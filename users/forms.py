from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(
            attrs={
                "class": "auth-input",
                "placeholder": "请输入用户名",
                "autofocus": True,
                "autocomplete": "username",
            }
        ),
    )
    password = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "auth-input",
                "placeholder": "请输入密码",
                "autocomplete": "current-password",
            }
        ),
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="邮箱",
        widget=forms.EmailInput(
            attrs={
                "class": "auth-input",
                "placeholder": "请输入邮箱",
                "autocomplete": "email",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "用户名"
        self.fields["username"].widget.attrs.update(
            {
                "class": "auth-input",
                "placeholder": "请输入用户名",
                "autocomplete": "username",
                "autofocus": True,
            }
        )

        self.fields["email"].label = "邮箱"
        self.fields["email"].widget.attrs.update(
            {
                "class": "auth-input",
                "placeholder": "请输入邮箱",
                "autocomplete": "email",
            }
        )

        self.fields["password1"].label = "密码"
        self.fields["password1"].widget.attrs.update(
            {
                "class": "auth-input",
                "placeholder": "设置密码",
                "autocomplete": "new-password",
            }
        )

        self.fields["password2"].label = "确认密码"
        self.fields["password2"].widget.attrs.update(
            {
                "class": "auth-input",
                "placeholder": "再次输入密码",
                "autocomplete": "new-password",
            }
        )

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("这个邮箱已经注册过了。")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
