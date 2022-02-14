from django.shortcuts import render


# Create your views here.
def markets(request):
    """ A view to return the index page """

    return render(request, 'markets.html')
