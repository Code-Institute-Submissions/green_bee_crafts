from django.shortcuts import render

# Create your views here.

def markets(request):
    """ A view to return the upcoming markets page """

    return render(request, 'markets/markets.html')
