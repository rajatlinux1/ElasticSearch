from django.shortcuts import render
from App.documents import UserDataDocument
from elasticsearch_dsl import Q
from . models import UserData
from django.http import JsonResponse
# Create your views here.
def search(request):
    if request.method == "POST":
        Name=request.POST.get('search').lower()
        City=request.POST.get('City')
        City=''
        print("..........................................................................................................................................................................")
        print(Name)
        print(City)
        print('Searching for information...', Name, City)
        if len(Name)!=0 and len(City)==0:
            response=UserDataDocument.search().query(Q("match", name=Name) | Q("prefix", name=Name))
            return render(request, 'search.html', {'content':response})
        elif len(Name)==0 and len(City)!=0:
            response=UserDataDocument.search().query(Q("match", city=City) | Q("prefix", city=City))
            return render(request, 'search.html', {'content':response})
    
        if Name or City:
            response=UserDataDocument.search().query(Q("match_phrase_prefix", name=Name) & Q("match_phrase_prefix", city=City))
            return render(request, 'search.html', {'content':response})
    return render(request, 'search.html')