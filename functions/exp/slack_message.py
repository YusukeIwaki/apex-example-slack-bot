# -*- coding:utf-8 -*-

import os
from urllib.parse import urlencode
from urllib.request import urlopen

class SlackMessage:
  def __init__(self, icon_emoji=None, username=None):
    self._token = os.environ.get('SLACK_API_TOKEN')
    self.icon_emoji = icon_emoji
    self.username = username

  def post(self, channel, body):
    return self._postMessage(channel, body, None)

  def reply(self, channel, ts, body):
    return self._postMessage(channel, body, ts)
    
  def _postMessage(self, channel, body, ts):
    method = 'POST'
    url = 'https://slack.com/api/chat.postMessage'

    params = {
      'token': self._token,
      'channel': channel,
      'text': body
    }
    if ts is not None:
      params["thread_ts"] = ts
    if self.icon_emoji is not None:
      params["icon_emoji"] = self.icon_emoji
    if self.username is not None:
      params["username"] = self.username

    if self._token is None:
      params["token"] = "! EMPTY !"
      print("ENV['SLACK_API_TOKEN'] is not set")
      print("---------------------------")
      print("")
      return "%s %s\n\n%s"%(method, url, params)

    with urlopen(url, urlencode(params).encode('ascii')) as res:
      #print(res.info())
      return res.read().decode("utf-8")

if __name__ == "__main__":
  slack = SlackMessage()
  print(slack.post("#playground2", "test"))