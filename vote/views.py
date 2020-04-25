from django.shortcuts import render
from .forms import VotingForm
from .models import Vote, VoteCounting
from exhibit.models import GalleryArt


def artvotes(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            chosen_art_options = form.cleaned_data.get('chosen_art_options', [])
            other_artname = form.cleaned_data.get('other_artname', '')
            Vote.bulk_vote(chosen_art_options + [other_artname])
        message = 'Thank You For Your Contribution!'
    elif request.method == 'GET':
        message = ''

    form = VotingForm()
    return render(request, 'vote.html', {'form': form, 'message': message})


def vote_counts(request):
    """A View that renders the votecounting on the contents page"""
    votecounts = VoteCounting.objects.all()
    return render(request, "vote.html", {"votecounts": votecounts})
