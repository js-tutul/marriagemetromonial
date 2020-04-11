from math import ceil

from django.shortcuts import render
from accounts.models import CompletedRegister

# Create your views here.
def Bhome(request):
    task=CompletedRegister.objects.all()
    n = len(task)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': task}

    allProds = []
    genders=CompletedRegister.objects.values('gender','id')
    cats={item['gender'] for item in genders}
    for cat in cats:
        prod=CompletedRegister.objects.filter(gender=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request,'BT/bloghome.html',params)
