from django.shortcuts import render


# Create your views here.
def markets(request):
    """ A view to return all markets """

    return render(request, 'markets/markets.html')
