from django.contrib.auth.model import BaseUserManager


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
