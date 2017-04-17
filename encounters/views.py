from django.shortcuts import render
from encounters.generator import random_encounter

# View functions
def encounters(request):
	random_encounter('Aquatic')
	if request.method == 'POST':
		return render(request, 'encounters/encounters.html')
	else:
		return render(request, 'encounters/encounters.html')