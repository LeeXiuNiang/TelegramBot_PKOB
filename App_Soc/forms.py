from django import forms
from .models import User
import re
from datetime import datetime
from dateutil import parser

#DataFlair
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('ic_no','name', 'phone_no')
        labels = {
            'ic_no': 'IC Number :',
            'name': 'Name :',
            'phone_no': 'Phone :',
        }
        widgets = {
            'ic_no': forms.TextInput(attrs={'class': 'textfield'}),
            #'ic_no': forms.TextInput(attrs={'class': 'textfield','pattern': '(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})'}),
            'name': forms.TextInput(attrs={'class': 'textfield'}),
            'phone_no': forms.TextInput(attrs={'class': 'textfield'}),
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['ic_no'].widget.attrs['readonly'] = True
            self.fields['name'].widget.attrs['readonly'] = True

    def clean(self):
        if not re.match(r'^[a-zA-Z]', self.cleaned_data['name']):
            msg = 'Numeric input is invalid for name'
            self.add_error('name', msg)

        if len(self.cleaned_data['ic_no']) != 12 or not re.match(r'^[0-9]', self.cleaned_data['ic_no']):
            msg = 'Invalid IC Number'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) > 12 or int(self.cleaned_data['ic_no'][2:4]) < 1:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][4:6]) < 1:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 1 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][0:2]) % 4 == 0 and int(self.cleaned_data['ic_no'][2:4]) == 2 \
                and int(self.cleaned_data['ic_no'][4:6]) > 29:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][0:2]) % 4 != 0 and int(self.cleaned_data['ic_no'][2:4]) == 2 \
                and int(self.cleaned_data['ic_no'][4:6]) > 28:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 3 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 4 and int(self.cleaned_data['ic_no'][4:6]) > 30:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 5 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 6 and int(self.cleaned_data['ic_no'][4:6]) > 30:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 7 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 8 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 9 and int(self.cleaned_data['ic_no'][4:6]) > 30:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 10 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 11 and int(self.cleaned_data['ic_no'][4:6]) > 30:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)
        elif int(self.cleaned_data['ic_no'][2:4]) == 12 and int(self.cleaned_data['ic_no'][4:6]) > 31:
            msg = 'Invalid birthday'
            self.add_error('ic_no', msg)

        if not re.match(r'^[0-9]', self.cleaned_data['phone_no']):
            msg = 'Alphabetical input is invalid for phone'
            self.add_error('phone_no', msg)

        return self.cleaned_data













