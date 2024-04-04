from django import forms
from .models import Post
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class SignUpForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

class PostForm(forms.ModelForm):
    class Meta:
      model = Post
      fields = ['title','desc',]
      labels = {'title':'Title','desc':'Description',}
      widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control',}),} 
      