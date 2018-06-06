import random
import string

import factory
from django.test import TestCase

from .models import Post


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class PostFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Post

    title = factory.LazyAttribute(lambda t: random_string())
    text = factory.LazyAttribute(lambda t: random_string())
