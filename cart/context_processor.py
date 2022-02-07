from . models import *
from . views import *

def count(request):
    item_count=0
    if 'admin' in request.path:  #using this for counting and how many item needs to delete
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(request)) #in views we use c_id function for creating id
            cti=items.objects.all().filter(cart=ct[:1])                    #for getting items #ct is the first element
            for c in cti:
                item_count += c.quantity #count the items
        except cartlist.DoesNotExist: #if element is not there
            item_count=0
        return dict(itc=item_count) #next we want to see this item_count in cart.html

