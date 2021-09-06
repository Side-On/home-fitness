from django import forms
from .models import Review


class UserReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('review_title', 'review_comment',)
