import factory
from flask_security.utils import hash_password

from udata.factories import ModelFactory

from .models import Role, User


class UserFactory(ModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Sequence(lambda n: "user{}@example.com".format(n))
    fs_uniquifier = factory.Faker("uuid4")
    active = True

    @classmethod
    def _adjust_kwargs(cls, **kwargs):
        if "password" in kwargs:
            # Password is stored hashed
            kwargs["password"] = hash_password(kwargs["password"])
        return kwargs


class AdminFactory(UserFactory):
    @factory.lazy_attribute
    def roles(self):
        admin_role, _ = Role.objects.get_or_create(name="admin")
        return [admin_role]
