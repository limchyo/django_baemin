from django.forms import ModelForm, TextInput, Textarea
from .models import Partner

# Create the form class.
class PartnerForm(ModelForm):
     class Meta:
         model = Partner
         fields = (
             'name',
             'contact',
             'address',
             'description'
         )
         widgets = {
            'name': TextInput(attrs={"class":"form-control"}),
            'contact': TextInput(attrs={"class":"form-control"}),
            'address': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"})
         }
