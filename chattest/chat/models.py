from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Room(models.Model):
	name = models.TextField()
	label = models.SlugField(unique = True)

	def __unicode__(self):
		return self.label

class Message(models.Model):
	room = models.ForeignKdy(Room, related_name = 'messages')
	handle = models.TextField()
	messages = models.TextField()
	timestamp = models.DateTimeField(default = timezone.now, db_index = True)

	def __unicode__(self):
		return '[{timestamp}] {handle}: {messages}'.format(**self.as_dict())

	@property
	def formatted_timestamp(self):
		return self.timestamp.strftime('%b %-d %-I: %M %p ')

	def as_dict(self):
		return {
			'handle' : self.handle,
			'messages' : self.messages,
			'timestamp' : self.formatted_timestamp
		}