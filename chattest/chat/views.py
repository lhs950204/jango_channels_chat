import random
import string

from django.db import transaction
from haikunator import Haikunator
from .models import Room

from django.shortcuts import render, redirect

# Create your views here.

def about(request):
	return render(request, "chat/about.html")

def nee_room(request):

	new_room = None

	while not new_room:
		with transaction.atomic():
			label = Haikunator.haikunator()
			if Room.objects.filter(label = label).exists():
				continue
			new_room = Room.objects.create(label = label)
	return redirect(chat_room, label = label)

def chat_room(request, label):

	room, created = Room.objects.get_or_create(label = label)
	messages = reversed(room.messages.order_by('-timestamp')[:50])

	return render(request, "chat/room.html",{
		'room' : room,
		'messages' : messages
		})