from django import forms
from .models import Vote


class VotingForm(forms.Form):
    chosen_art_options = forms.MultipleChoiceField(choices=(), label='Art from the Galleries', required=False,
                                                     widget=forms.SelectMultiple(
                                                        attrs={
                                                             'class': 'form-control'
                                                         }
                                                     ))
    other_art_name = forms.CharField(label='Other', max_length=100, required=False,
                                      widget=forms.TextInput(
                                        attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Other suggestions'
                                          }
                                      ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        unique_artnames = Vote.objects.order_by('artname').values_list('artname', flat=True).distinct()
        self.fields['chosen_art_options'].choices = [(artname, artname) for artname in unique_artnames]