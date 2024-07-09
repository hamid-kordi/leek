from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, name, phone_number, password):
        if not email:
            raise ValueError("User most have an email address")
        if not phone_number:
            raise ValueError("user most have phone_number")
        if not name:
            raise ValueError("user not have name?")
        user = self.model(
            user_name=user_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password, user_name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            name=name,
            phone_number=phone_number,
            password=password,
            user_name=user_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
