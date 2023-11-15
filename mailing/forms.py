from django import forms
from mailing.models import Mailing, Message, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        uid = kwargs.pop('uid')
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(user=uid)
        self.fields['message'].queryset = Message.objects.filter(user=uid)

    class Meta:
        model = Mailing
        exclude = ('user',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)
