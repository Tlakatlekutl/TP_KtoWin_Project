from django import forms
from .models import Post, UserProfile, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'game', 'post_type']


class SignupUserForm(forms.ModelForm):
    password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput)

    def clean_password2(self):
        # print(self.cleaned_data['password'])
        if self.cleaned_data.get('password2') != self.cleaned_data.get('password'):
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(SignupUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class SettingsNickname(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class SignupProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'avatar']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class ChangePasswordForm(forms.ModelForm):
    password2 = forms.CharField(label="Повторите пароль",
                                widget=forms.PasswordInput)

    def clean_password2(self):
        # print(self.cleaned_data['password'])
        if self.cleaned_data.get('password2') != self.cleaned_data.get('password'):
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(ChangePasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(),
        }
