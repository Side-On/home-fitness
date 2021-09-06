from django import forms
from .models import Review


class UserReviewForm(forms.ModelForm):

    class Meta:
        model: Review
        fields = ('review-title', 'review-comment')
