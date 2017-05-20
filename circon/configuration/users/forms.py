from django import forms


class CreateForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput())
    first_name = forms.CharField(label="Nombre",
                                 required=False, widget=forms.TextInput())
    last_name = forms.CharField(label="Apellido", required=False,
                                widget=forms.TextInput())
    email = forms.EmailField(label="Correo", required=False,
                             widget=forms.TextInput())
    is_active = forms.CharField(label="Activo", required=False,
                                widget=forms.TextInput())
    password = forms.CharField(label="Password", required=False,
                               widget=forms.PasswordInput(render_value=True))
    password_two = forms.CharField(label="Confirmar password",
                                   required=False,
                                   widget=forms.PasswordInput(render_value=True))
    company = forms.CharField(label="Company", required=False,
                              widget=forms.TextInput())
    address = forms.CharField(label="Address", required=False,
                              widget=forms.TextInput())
    phone = forms.CharField(label="Phone", required=False,
                            widget=forms.TextInput())
    rif = forms.CharField(label="Rif", required=False,
                          widget=forms.TextInput())
    provider = forms.CharField(label="Provider", required=False,
                               widget=forms.TextInput())
    customer = forms.CharField(label="Customer", required=False,
                               widget=forms.TextInput())

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         p = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #     raise forms.ValidationError('Nombre de usuario ya existe')

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     try:
    #         p = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return email
    #     raise forms.ValidationError('Email ya registrado')

    # def clean_password_two(self):
    #     password = self.cleaned_data['password']
    #     password_two = self.cleaned_data['password_two']
    #     if password == password_two:
    #         pass
    #     else:
    #         raise forms.ValidationError('Password no coinciden')


class ChangePasswordForm(forms.Form):

    current_password = forms.CharField(
        label='current password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='New password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password_two = forms.CharField(
        label='Repeat password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password_two(self):
        """Comprueba que password y password_two sean iguales."""
        password = self.cleaned_data['password']
        password_two = self.cleaned_data['password_two']
        if password != password_two:
            raise forms.ValidationError('Los password no coinciden.')
        return password_two
