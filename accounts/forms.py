from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class Errors(ErrorList):
    def __str__(self):
        if not self:
            return ''
        
        return mark_safe(''.join([
            f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self
        ]))


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for input_field in ['username', 'password1', 'password2']:
            self.fields[input_field].help_text = None
            self.fields[input_field].widget.attrs.update({'class': 'form-control'})
