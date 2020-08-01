from django import forms 
from django.forms import ModelForm 
from .models import NewsStory 



class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form',
                    'placeholder': 'Select a date',
                    'class': 'inputbox',
                    'type': 'date'
                }
            ), 

            'title': forms.TextInput(
                attrs={
                    'class': 'form',
                    'class': 'inputbox',
                    'placeholder': 'Title Name'
                }
            ),
            
            'author': forms.TextInput(
                attrs={
                    'class': 'form',
                    'class': 'inputbox',
                    'placeholder': 'Author Name'
                }
            ),
            
            'content': forms.Textarea(
                attrs={
                    'class': 'form', 
                    'class': 'inputbox',
                    'placeholder': 'Enter Content Here'
                }
            )
        }

