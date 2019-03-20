# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
Event_Type = (
    ('bridal','Bridal'),
    ('bridal shower', 'Bridal Shower'),
    ('engagement','Engagement'),
    ('baby shower', 'Baby Shower'),
    ('birthday', 'Birthday'),
    ('school event', 'School Event'),
    ('friends/family reunion', 'Friends/Family ReUnion'),
    ('others', 'Others'),
)
class ContactUs(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    EventDate = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)
    EventType= models.CharField(max_length=50, choices=Event_Type, default='bridal')
    Message = models.CharField(max_length=200)



    def __str__(self):
        return self.Name