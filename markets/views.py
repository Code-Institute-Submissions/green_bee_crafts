from django.shortcuts import render
from .models import Market


# Create your views here.
def markets(request):
    """ A view to return all markets """
    markets = Market.objects.all()    

    context = {
        'markets': markets
    }

    return render(request, 'markets/markets.html', context)
