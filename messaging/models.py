from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="pending")  # e.g., sent, delivered, failed

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}..."