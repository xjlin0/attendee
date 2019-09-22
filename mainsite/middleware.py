import pytz
from urllib import parse
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = parse.unquote(request.COOKIES['timezone'])
        print("getting user time zone as " + tzname)
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
