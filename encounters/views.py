from django.shortcuts import render

# Create your views here.
def encounters(request):
	return render(request, 'encounters/encounters.html')