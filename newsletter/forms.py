from django import forms
class EmailCaptureForm(forms.Form):
    email = forms.EmailField(label="Email Address",required=True,error_messages={
        "required": "Please enter your email address",
        "invalid": "Please enter a valid email address"},
        widget = forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}))
