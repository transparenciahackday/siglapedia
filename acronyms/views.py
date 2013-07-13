from django.shortcuts import render_to_response
from acronyms.models import Acronym

def fetch(request):
    if request.GET.get('q'):
        results = Acronym.objects.filter(name=request.GET.get('q'))
        if not results:
            return render_to_response('notfound.html')

        return render_to_response('found.html', {'results': results})
        
