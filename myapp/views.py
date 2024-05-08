from django.shortcuts import render
from .models import Message
from django.http import JsonResponse

# Create your views here.
def message_list(request):
    messages = Message.objects.all().values("id", "text")
    return JsonResponse(list(messages), safe=False)