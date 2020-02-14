import random
import string

from django.core.validators import URLValidator

from short_url.models import ShortURL

random_string_length = 10


def random_string(string_length):
    """Generate a random string with the combination of lowercase and uppercase letters """

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))


def create_short_link(main_link, short_link, user):
    url = ShortURL.objects.filter(short_link=short_link)
    if main_link and url.count() == 0 and my_validate_url(main_link):
        if not short_link:
            short_link = random_string(random_string_length)
        ShortURL.objects.create(main_link=main_link, short_link=short_link, owner=user)
        return True
    return False


def my_validate_url(url):
    validate = URLValidator()
    try:
        validate(url)
        return True
    except:
        return False
