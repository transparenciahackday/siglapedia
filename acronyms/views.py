from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from acronyms.models import Acronym, AcronymForm

def fetch(request):
    q = request.GET.get('q')
    if q and request.GET.get('format') == "json":
        results = Acronym.objects.filter(name=q)
        jsondata = serializers.serialize('json', results, ensure_ascii=False, 
                fields=("name", "definition", "description", "link"))
        return HttpResponse(jsondata, mimetype="application/json")
    elif q:
        results = list(Acronym.objects.filter(name=q))
        if not results:
            return render(request, 'add.html', {'querystring': q, 'notfound': True,
                                                     'form': AcronymForm(initial={'name': q})})
        return render(request, 'results.html', {'results': results})
        
def add(request):
    if request.method == 'POST':
        form = AcronymForm(request.POST)
        if form.is_valid():
            acronym = form.save()
            return render(request, 'results.html', {'results': [acronym,], 'new_entry': True})
    else:
        form = AcronymForm(initial={'name': request.GET.get('q')})
    return render(request, 'add.html', {'form': form})

