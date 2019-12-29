from django.contrib.auth.models import BaseUserManager, UserManager


class CustomModelManager(BaseUserManager):
    def get_or_none(self, **kargs):
        try:
            return self.get(**kargs)
        except self.model.DoesNotExist:
            return None


class CustomUserManager(CustomModelManager, UserManager):
    pass
