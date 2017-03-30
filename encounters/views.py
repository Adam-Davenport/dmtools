from django.shortcuts import render

# View functions
def encounters(request):
	return render(request, 'encounters/encounters.html')