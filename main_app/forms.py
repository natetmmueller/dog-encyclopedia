from django.forms import ModelForm
from .models import Walks

class WalksForm(ModelForm):
    class Meta:
        model = Walks
        fields = ['date', 'time']