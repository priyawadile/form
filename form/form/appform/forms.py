from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100)
    sponsor_names = forms.CharField(label='Sponsor Names', widget=forms.TextInput(attrs={'class': 'sponsor-input'}))
