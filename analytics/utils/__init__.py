import _thread

from django.shortcuts import get_object_or_404

from analytics.models import URLObservation, UserObservation
from short_url.models import ShortURL


def record_observations(request, short_link):
    _thread.start_new_thread(record_url_observation, (request, short_link))
    _thread.start_new_thread(record_user_observation, (request, short_link))


def record_url_observation(request, short_link):
    short_url = get_object_or_404(ShortURL, short_link=short_link)
    browser = get_browser_type(request.user_agent.browser.family)
    device = 0 if request.user_agent.is_mobile else 1
    URLObservation.objects.create(short_url=short_url, browser=browser, device=device)


def record_user_observation(request, short_link):
    short_url = get_object_or_404(ShortURL, short_link=short_link)
    if UserObservation.objects.filter(short_url=short_url, owner_ip=request.META['REMOTE_ADDR']).count() == 0:
        browser = get_browser_type(request.user_agent.browser.family)
        device = 0 if request.user_agent.is_mobile else 1
        UserObservation.objects.create(short_url=short_url, browser=browser, device=device,
                                       owner_ip=request.META['REMOTE_ADDR'])


def get_browser_type(browser_name):
    if 'chrome' in browser_name.lower():
        return 0
    if 'mozilla' in browser_name.lower():
        return 1
    if 'safari' in browser_name.lower():
        return 2
    if 'iE' in browser_name.lower():
        return 3
    if 'opera' in browser_name.lower():
        return 4
    return 5