from django import forms
from .models import Vote


class VotingForm(forms.Form):
    chosen_art_options = forms.MultipleChoiceField(choices=[], label='Art', required=False,
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
        unique_galleryarts = Vote.objects.order_by('galleryart').values_list('galleryart', flat=True).distinct()
        self.fields['chosen_art_options'].choices = [(galleryart, galleryart) for galleryart in unique_galleryarts]