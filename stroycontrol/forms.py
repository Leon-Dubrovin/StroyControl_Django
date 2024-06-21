from django import forms
class LoginForm(forms.Form):
    login = forms.CharField(
        min_length=2,
        max_length=20,
        label="Логин",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        min_length=5,
        max_length=20,
        label="Пароль",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
class UserForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя (Логин)',
            }
        )
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия пользователя',
            }
        )
    )
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )
    email = forms.EmailField(
        required=False,
        min_length=7,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
            }
        )
    )
    age = forms.IntegerField(
        help_text="Введите свой возраст",
        min_value=14,
        max_value=120,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Возраст',
            }
        )
    )