import unittest

from unittest.mock import call, patch
import slack_event_router, exp_router
import uuid

class TestSlackEventRouter(unittest.TestCase):
  def test_edited_message_is_not_handled(self):
    body = {
      "event": {
        "type": "message",
        "user": "U012CRRR3",
        "text": "hoge",
        "client_msg_id": str(uuid.uuid4()),
        "edited": {
          "user": "U012CRRR3",
          "ts": "1538623446.000000"
        },
        "ts": "1538623325.000100",
        "channel": "C0ABCD1EF",
        "event_ts": "1538623325.000100"
      }
    }

    with patch.object(exp_router, "router") as mockRouter:
      slack_event_router.handle_event(body)
      mockRouter.handle.assert_not_called()
