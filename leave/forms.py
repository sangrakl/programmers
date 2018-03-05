from django.forms import *
from .models import *

class RegistForm(ModelForm):
    class Meta:
        model = Leave
        fields = [
        'startDate',
        'startTime',
        'endDate',
        'endTime',
        'briefs']
