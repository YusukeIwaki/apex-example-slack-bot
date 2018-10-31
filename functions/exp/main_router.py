# -*- coding:utf-8 -*-

from base_routers import Router
import slack_event_router
import json
import os

router = Router()

'''
POST /hoge?param1=p1
{
  "hoge": "hoge1"
}
のときは
event:
  httpMethod: POST
  resource: /hoge
  body: "{ "hoge": "hoge1" }"
  queryStringParameters: {'param1': 'p1'}
  
----
注意:
https://api.slack.com/events-api にあるように
Responding to Events
Your app should respond to the event request with an HTTP 2xx within three seconds. If it does not, we'll consider the event delivery attempt failed. After a failure, we'll retry three times, backing off exponentially.
Maintain a response success rate of at least 5% of events per 60 minutes to prevent automatic disabling.
---
200系のレスポンスを返さないとリトライになるし、
あまりに失敗が多いとdisableされちゃうらしい。
'''

@router.Route("POST /exp")
def handle_cw_alert_helper(event):
  jsonBody = json.loads(event["body"])
  verification_token = os.environ.get('SLACK_APP_VERIFICATION_TOKEN')
  if verification_token is not None and jsonBody["token"] == verification_token:
    body = "OK"
    if "X-Slack-Retry-Num" in event["headers"]:
      print("SKIP", event["headers"]["X-Slack-Retry-Num"])
    else:
      try:
        ret = slack_event_router.router.handle(jsonBody["type"], jsonBody)
        if ret is not None:
          body = ret
      except Exception as e:
        print("ERROR", e)

    # 何が何でも200を返す
    return {
      "statusCode": 200,
      "headers": {
        "Content-Type": "text/plain"
      },
      "body": body
    }
  else:
    return not_found(event)

@router.DefaultRoute
def not_found(event):
  return {
    "statusCode": 404,
    "headers": {
      "Content-Type": "text/plain"
    },
    "body": "Not Found"
  }