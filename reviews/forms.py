from django import forms
from .models import *


class UserReviewForm(forms.ModelForm):

    class Meta:
        model: Review
        fields = ('title', 'comment')
