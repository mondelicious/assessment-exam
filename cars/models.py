import uuid

from django.db import models
from django.conf import settings


class Colors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Car Color"
        verbose_name_plural = "Car Colors"
        ordering = ['-name']
    
    def __str__(self):
        return "%s" % (self.name)


class Cars(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    color = models.ForeignKey(Colors, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'List of Car'
        verbose_name_plural = 'List of Cars'
        ordering = ['-name']
    
    def __str__(self):
        return "%s - %s" %(self.name, self.color)

