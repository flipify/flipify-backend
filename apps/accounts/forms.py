from typing import Any

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class BaseUserForm(forms.ModelForm):
    """Default user registration form"""

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email"]

    def clean_email(self) -> str:
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("user with this email already exists")
        return email

    def clean(self) -> dict[str, Any]:
        """Verify both passwords"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "password mismatch!")
        return cleaned_data


class RegisterForm(BaseUserForm):
    ...


class UserAdminCreationForm(BaseUserForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the field on the user,
    but replaces the password field with the admin's password hash
    display field."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        models = User
        fields = ["email", "password", "is_active", "is_superuser"]

    def clean_password(self):
        return self.initial["password"]
