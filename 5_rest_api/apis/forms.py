from django import forms

class SchoolNameFilterForm(forms.Form):
    name = forms.CharField(max_length=250)
