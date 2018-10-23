from __future__ import unicode_literals

from django.db import models

# Create your models here.

LIGHT_POWER = (
    ("0", "off"),
    ("1", "on"),
)

class Light(models.Model):
    status = models.CharField(max_length = 2, choices=LIGHT_POWER, verbose_name="Statut", default="0")

    def __unicode__(self):
        return "Light #%s: %s" % (self.id, self.status)
