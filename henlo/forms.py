from django import forms
from henlo.models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # Note: the trailing comma IS required
