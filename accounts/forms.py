from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for input_field in ['username', 'password1', 'password2']:
            self.fields[input_field].help_text = None
            self.fields[input_field].widget.attrs.update({'class': 'form-control'})
