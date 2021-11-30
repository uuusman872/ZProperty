from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, PropertyInquiry
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Username",
        "data-rule" : "minlen:4",
        "data-msg" : "Please enter at least 4 chars.",

    }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Email",
        "data-rule" : "email",
        "data-msg" : "Please enter a valid email.",
    }))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
       "class": "form-control form-control-lg form-control-a",
        "placeholder": "First Name",
        "data-rule" : "minlen:3",
        "data-msg" : "Please enter at least 3 chars.",
    }))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Last Name",
        "data-rule" : "minlen:3",
        "data-msg" : "Please enter at least 3 chars.",
    }))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Password",
        "data-rule" : "minlen:8",
        "data-msg" : "Please enter at least 8 chars of password.",
        "type":"password"
    }))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Confirm Password",
        "data-rule" : "minlen:8",
        "data-msg" : "Please enter at least 8 chars of password.",
        "type":"password"
    }))
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class QuestionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Full Name",
        "data-rule" : "minlen:4",
        "data-msg" : "Please enter at least 4 chars.",

    }))

    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Email",
        "data-rule" : "email",
        "data-msg" : "Please enter a valid email.",
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
       "class": "form-control form-control-lg form-control-a",
        "placeholder": "Phone#",
        "data-rule" : "minlen:4",
        "data-msg" : "Please enter a valid phone number.",
        "type":"number"
    }))

    Subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Subject",
        "data-rule" : "minlen:4",
        "data-msg" : "Please enter at least 8 chars of subject.",
    }))
    Question = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Message",
        "data-msg" : "Please write something for us.",
        "rows" :"6"
    }))

    class Meta:
        model = Question
        fields = ["name", "email", "phone", "Subject", "Question"]


class PropertyInquiryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Full Name",
        "data-msg" : "Please enter at least 4 chars.",

    }))

    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Email",
        "data-rule" : "email",
        "data-msg" : "Please enter a valid email.",
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
       "class": "form-control form-control-lg form-control-a",
        "placeholder": "Phone#",
        "data-msg" : "Please enter a valid phone number.",
        "type":"number"
    }))

    Subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control form-control-lg form-control-a",
        "placeholder": "Subject",
        "data-msg" : "Please enter at least 8 chars of subject.",
    }))
    Question = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Message",
        "data-msg" : "Please write something for us.",
        "rows" :"6"
    }))

    class Meta:
        model = PropertyInquiry
        fields = ["name", "email", "phone", "Subject", "Question"]
