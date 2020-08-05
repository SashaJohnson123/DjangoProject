from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget

from .models import NewsStory


class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )

    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form',
                    'class': 'inputbox',
                    'placeholder': 'Title Name'
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
