import unittest

from unittest.mock import call, patch
import main
import os
import secrets

class TestMain(unittest.TestCase):
  def test_handle(self):
    verification_token = os.environ.get('SLACK_APP_VERIFICATION_TOKEN')
    challenge = secrets.token_urlsafe(32)
    event = {
      "httpMethod": "POST",
      "resource": "/exp",
      "headers": {},
      "body": "{ \"token\": \""+ verification_token +"\", \"challenge\": \""+ challenge +"\", \"type\": \"url_verification\" }"
    }
    context = None
    response = main.handle(event, context)
    self.assertEqual(response["body"], challenge)