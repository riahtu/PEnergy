from django.db import models
from django.conf import settings
# Create your models here.
class House(models.Model):
  label = models.CharField(max_length=128, blank=False, unique=True)
  creation_date = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
  last_modified = models.DateTimeField(auto_now=True, blank=True)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="house")
