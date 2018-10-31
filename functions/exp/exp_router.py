# -*- coding:utf-8 -*-

from base_routers import RegexRouter
import slack_message
import json

router = RegexRouter()
slack = slack_message.SlackMessage(icon_emoji = ":+1:")

@router.Route("^ping$")
def handle_ping(event):
  slack.reply(event["channel"], event["ts"], "pong")

@router.DefaultRoute
def not_handled(event):
  return "Not handled in exp_router"