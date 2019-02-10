from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
# Create your views here.

def seguimiento(request): #agregado
	


    static_url=settings.STATIC_URL
    tipo_side = 1
    return render('reports/seguimiento.html', locals(),
            context_instance=RequestContext(request))
