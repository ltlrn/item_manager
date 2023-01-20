from django.shortcuts import get_object_or_404, redirect, render

from .forms import DiseaseForm

def index(request):
    form = DiseaseForm(request.POST or None)
    if request.method == 'POST':        
        if form.is_valid():
            form.save()
        
    context = {
        'form': form
    }

    return render(request, 'diseases/index.html', context)

