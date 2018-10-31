import unittest

import exp_router, slack_message

from unittest.mock import patch, call
import re

class StringWithPattern:
  def __init__(self, regex):
    self.re = re.compile(regex)
  def __eq__(self, other):
    return self.re.match(other) is not None

class StringContaining:
  def __init__(self, *substrings):
    self.substrings = substrings
  def __eq__(self, other):
    for substring in self.substrings:
      if not substring in other:
        return False
    return True

class TestExpRouter(unittest.TestCase):
  def test_ping(self):
    event = {
      "type": "message",
      "user": "U1234567",
      "text": "ping",
      "client_msg_id": "xxx",
      "ts": "1538626390.000100",
      "channel": "C0123456",
      "event_ts": "1538626390.000100"
    }
    with patch.object(slack_message.SlackMessage, "reply") as mock_reply:
      exp_router.handle_ping(event)
      mock_reply.assert_called_once_with("C0123456", "1538626390.000100", StringContaining("pong"))