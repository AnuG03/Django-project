from django.db.models import Q
from django.shortcuts import render
from shop.models import product

def search(request):
    b=None
    query=""
    if(request.method=="POST"):
        query=request.POST['s']
        print(query)
        if query:
            b=product.objects.filter(Q(name__icontains=query) | Q (price__icontains=query))     # django lookups
    context={'product': b, 'query': query}
    return render(request,'search.html',context)
