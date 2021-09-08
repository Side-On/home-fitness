from django import forms
from .models import FitTip


class FitTipForm(forms.ModelForm):

    class Meta:
        model = FitTip
        fields = ('fit_tip_title', 'fit_tip',)
