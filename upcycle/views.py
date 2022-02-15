from django.shortcuts import render
from .models import Upcycle


# Create your views here.
def upcycle(request):
    """ A view to return all upcycling information """
    upcycle = Upcycle.objects.all()    

    context = {
        'upcycle': upcycle
    }

    return render(request, 'upcycle/upcycle.html', context)
