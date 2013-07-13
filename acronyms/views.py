from django.shortcuts import render
from acronyms.models import Acronym, AcronymForm

def fetch(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        results = Acronym.objects.filter(name=q)
        if not results:
            return render(request, 'add.html', {'querystring': q, 'notfound': True,
                                                     'form': AcronymForm(initial={'name': q})})
        return render(request, 'found.html', {'results': results})
        
def add(request):
    if request.method == 'POST':
        form = AcronymForm(request.POST)
        if form.is_valid():
            acronym = form.save()
            return render(request, 'found.html', {'results': [acronym,]})
    else:
        form = AcronymForm(initial={'name': request.GET.get('q')})
    return render(request, 'add.html', {'form': form})

