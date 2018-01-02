from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    the purpose of this class is to more easily
    extend the user model in the future.
    """

    def __str__(self):
        return str(self.username)
