from django.shortcuts import render
from django.template import RequestContext
from . models import Results

def results_list(request):
	results = Results.objects.filter(regnumber='BED/20164/81/DF').order_by('examperiod')
	return render(request,'portal/results.html', {'results': results})