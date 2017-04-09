from django.shortcuts import render

# View functions
def encounters(request):
	if request.method == 'POST':
		return render(request, 'encounters/encounters.html')
	else:
		return render(request, 'encounters/encounters.html')