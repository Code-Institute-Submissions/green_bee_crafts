from django.shortcuts import render


# Create your views here.
def upcycle(request):
    """ A view to return the index page """

    return render(request, 'upcycle/upcycle.html')
