from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import send_whatsapp_message

logger = logging.getLogger(__name__)

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            sender = data.get('sender')
            receiver = data.get('receiver')
            content = data.get('content')

            # Save the incoming message
            message = Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content,
                status="received"
            )
            logger.info(f"Message received from {sender}: {content}")
            return JsonResponse({"status": "success", "message_id": message.id}, status=200)
        except Exception as e:
            logger.error(f"Error processing webhook: {e}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@api_view(['POST'])
def send_message(request):
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    content = request.data.get('content')

    if not all([sender, receiver, content]):
        return Response({"status": "error", "message": "Missing required fields"}, status=400)

    message = send_whatsapp_message(sender, receiver, content)
    if message:
        return Response({"status": "success", "message_id": message.id}, status=200)
    else:
        return Response({"status": "error", "message": "Failed to send message"}, status=500)