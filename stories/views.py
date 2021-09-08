from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from profiles.models import User
from stories.models import Story

# Create your views here.


def all_stories(request):

    stories = Story.objects.all()

    context = {
        'stories': stories,
    }
    return render(request, 'stories/stories.html', context)
