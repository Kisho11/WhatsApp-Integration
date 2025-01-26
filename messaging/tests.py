from django.test import TestCase, Client
from .models import Message

class MessagingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_webhook(self):
        response = self.client.post(
            '/api/webhook/',
            data={'sender': '123', 'receiver': '456', 'content': 'Hello'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)

    def test_send_message(self):
        response = self.client.post(
            '/api/send/',
            data={'sender': '123', 'receiver': '456', 'content': 'Hello'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Message.objects.count(), 1)