from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


User = get_user_model()


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザー名')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません。')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    picture = forms.FileField(required=False)
    website = forms.URLField(required=False)
    circle = forms.CharField(label='サークル名', required=False)
    circle_info = forms.CharField(label='活動内容', required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'picture', 'website', 'circle', 'circle_info']
    
    def clean_password(self):
        return self.initial['password']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザー名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    picture = forms.FileField(label='トップ画像', required=False)
    website = forms.URLField(required=False)
    circle = forms.CharField(label='サークル名', required=False)
    circle_info = forms.CharField(label='活動内容', required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'picture', 'website', 'circle', 'circle_info']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('password', )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません。')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user