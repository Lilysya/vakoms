import factory
from django.contrib.auth.models import User
from factory import DjangoModelFactory, lazy_attribute


class UserFactory(DjangoModelFactory):
    first_name = 'Shirisha'
    last_name = 'Gaddi'
    username = factory.Sequence(lambda n: 'user_%d' % n)
    email = lazy_attribute(lambda obj: obj.username + "@example.com")

    class Meta:
        model = User
        django_get_or_create = ('username',)