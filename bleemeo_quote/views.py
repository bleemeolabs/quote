from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from bleemeo_quote.models import Quote


@cache_page(settings.QUOTE_CACHE_DURATION)
def index(request):
    quote = Quote.objects.order_by("?").first()

    return HttpResponse(
        "%s\n  -- %s" % (quote.quote, quote.author.name), content_type="text/plain"
    )
