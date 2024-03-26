from django.shortcuts import render
from .forms import EventForm

# Create your views here.
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_name = form.cleaned_data['event_name']
            sponsor_names = form.cleaned_data.getlist('sponsor_names')
            # Process the form data (e.g., save to the database)
            # Redirect to a success page or return a success message
    else:
        form = EventForm()
    return render(request, 'template.html', {'form': form})