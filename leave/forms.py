from django.forms import *
from .models import *
from django.utils.translation import gettext_lazy as _

class RegistForm(ModelForm):
    class Meta:
        model = Leave
        fields = [
        'startDate',
        'startTime',
        'endDate',
        'endTime',
        'briefs']
        labels = {
        'startDate': _('시작날짜'),
        'startTime': _('시작시간'),
        'endDate': _('종료날짜'),
        'endTime': _('종료시간'),
        'briefs': _('사유')
        }
        help_texts = {
        'briefs': _('휴가 사유를 간단하게 남겨주세요')
        }
        widgets = {
            'startDate': DateInput(attrs={'class': 'dateCalendar'}),
            'endDate' : DateInput(attrs={'class': 'dateCalendar'}),
        }

class ContactForm(Form):
    subject = CharField(max_length=100)
    message = CharField()
    sender = EmailField()
    cc_myself = BooleanField(required=False)
