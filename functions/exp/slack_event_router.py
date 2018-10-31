# -*- coding:utf-8 -*-

from base_routers import Router
import exp_router

router = Router()

@router.Route("url_verification")
def handle_url_verification(jsonBody):
  return jsonBody["challenge"]

@router.Route("event_callback")
def handle_event(jsonBody):
  event = jsonBody["event"]

  if event["type"] != "message":
    return "Not handled: not message"

  if "edited" in event:
    return "Not handled: edited"

  ret = exp_router.router.handle(event["text"], event)
  if ret is None:
    return "Handled"
  else:
    return ret
    

@router.DefaultRoute
def not_handled(jsonBody):
  return "Not handled"