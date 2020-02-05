from django.contrib.auth import get_user_model

from django import forms
import email

User = get_user_model()

class AccountForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password does not match"
            )
    def clean_email(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError("This email is already in use!")
        return email