from django.http import HttpResponse
from bleemeo_quote.models import Quote


def index(request):
    quote = Quote.objects.order_by('?').first()

    return HttpResponse(
        "%s\n  -- %s" % (quote.quote, quote.author.name),
        content_type='text/plain'
    )
