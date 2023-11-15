from django import forms

from car.models import Car, Owner, CarHistory


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OwnerForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if cleaned_data:
            if not cleaned_data.endswith('@') and '@' not in cleaned_data:
                raise forms.ValidationError('Должен быть введен адрес почты ')
        else:
            raise forms.ValidationError('Должен быть введен адрес почты ')
        return cleaned_data


class CarForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        exception_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                           'обман', 'полиция', 'радар')
        for word in cleaned_data.split():
            if word.lower() in exception_words:
                raise forms.ValidationError('Такое слово нельзя вводить !!!')

        return cleaned_data




class CarHistoryForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = CarHistory
        fields = '__all__'
