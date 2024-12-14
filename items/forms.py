from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Item.objects.filter(name=name).exists():
            raise forms.ValidationError("An item with this name already exists. Please choose a different name.")
        return name
