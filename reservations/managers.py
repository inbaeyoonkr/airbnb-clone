from django.db import models


class CustomReservationManager(models.Manager):
    def get_or_none(self, **kargs):
        try:
            return self.get(**kargs)
        except self.model.DoesNotExist:
            return None
