from django import forms


class Message_form(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان ...', 'class': 'form-input'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام ...', 'class': 'form-input'}))
