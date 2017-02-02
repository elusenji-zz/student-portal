from . models import Results

def namez(request):
	return {'namez': Results.objects.all()}