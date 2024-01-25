# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label=""),
    description = forms.Textarea(),
    quantity = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Quantity", "class":"form-control"}), label=""),
    price = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Price", "class":"form-control"}), label=""),
    category = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Category", "class":"form-control"}), label=""),

    class Meta:
        model = Product   
        fields = ('name', 'description', 'quantity', 'price', 'category')