from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ a view to return the bag contents page """


    return render(request, 'bag/bag.html')


