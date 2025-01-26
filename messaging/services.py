import requests
import logging
from .models import Message

logger = logging.getLogger(__name__)

def send_whatsapp_message(sender, receiver, content):
    try:
        # Simulate sending a message via WhatsApp API
        # Replace with actual API call to WhatsApp
        response = requests.post(
            "https://api.whatsapp.com/send",  # Placeholder URL
            json={"sender": sender, "receiver": receiver, "content": content}
        )
        if response.status_code == 200:
            # Save the sent message
            message = Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content,
                status="sent"
            )
            logger.info(f"Message sent to {receiver}: {content}")
            return message
        else:
            logger.error(f"Failed to send message: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        return None