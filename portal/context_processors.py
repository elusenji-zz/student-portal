from portal.results.models import Result

def namez(request):
	return {'namez': Result.objects.all()}