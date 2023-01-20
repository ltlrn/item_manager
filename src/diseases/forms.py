from django import forms

from .models import Disease, Symptom


class DiseaseForm(forms.ModelForm):

    class Meta:
        model = Disease
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Положите сюда болезнь',
                    'class': 'form-control',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Опишите ее',
                    'class': 'form-control',
                }
            )        
        }

