from django.shortcuts import render

from .forms import VotingForm
from .models import Vote


def artvotes(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            chosen_art_options = form.cleaned_data.get('chosen_art_options', [])
            other_galleryart = form.cleaned_data.get('other_galleryart', '')
            Vote.bulk_vote(chosen_art_options + [other_galleryart])
        message = 'Thank You For Your Contribution!'
    elif request.method == 'GET':
        message = ''

    form = VotingForm()
    return render(request, 'vote.html', {'form': form, 'message': message})
