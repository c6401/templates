from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class ModelManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


@python_2_unicode_compatible
class Model(models.Model):
    """"""
    name = models.CharField(max_length=255, help_text=_("Name"))

    objects = ModelManager()

    class Meta:
        unique_together = (
            ('name',),
        )

    def __str__(self):
        return self.name

    def natural_key(self, name):
        return (self.name)
