from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Post

class ExampleForm(UserCreationForm):
    ROLES = [
        ("creator", "Creator"),
        ("reader", "Reader"),
    ]
    role = forms.ChoiceField(choices=ROLES, required=True)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email", "age", "role"
        )
