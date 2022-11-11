from django import forms
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, SetPasswordForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


def phone_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요.')


def student_id_validator(value):
    if len(str(value)) != 8:
        raise forms.ValidationError('본인의 학번 8자리를 입력해주세요.')


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False
        })
        self.fields['password1'].label = '비밀번호 확인'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['password2'].label = '비밀번호'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['interest'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['belong'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['rank'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['bachelor'].label = '학사'
        self.fields['bachelor'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['master'].label = '석사'
        self.fields['master'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['doctor'].label = '박사'
        self.fields['doctor'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'phone', 'interest', 'belong', 'rank', 'bachelor', 'master', 'doctor']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        print(user.bachelor)
        user.level = '2'
        user.save()
        user.is_active = False
        return user


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '이메일을 입력해주세요.'},
        label='이메일'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '비밀번호를 입력해주세요.'},
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '이메일이 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')


class RecoveryIdForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput,)
    phone = forms.CharField(widget=forms.TextInput,)

    class Meta:
        fields = ['name', 'phone']

    def __init__(self, *args, **kwargs):
        super(RecoveryIdForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_name',
        })
        self.fields['phone'].label = '연락처'
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_phone'
        })


class RecoveryPwForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput, )
    name = forms.CharField(
        widget=forms.TextInput,)
    phone = forms.CharField(
        widget=forms.TextInput, )

    class Meta:
        fields = ['email', 'name', 'phone']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_name',
        })
        self.fields['phone'].label = '연락처'
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_phone',
        })


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })


class CustomUserChangeForm(UserChangeForm):
    password = None
    phone = forms.CharField(label='연락처', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'11', 'oninput':"maxLengthCheck(this)",}),
    )
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', }),
    )
    interest = forms.CharField(label='관심 분야', widget=forms.TextInput(
        attrs={'class': 'form-control', }),
    )
    belong = forms.CharField(label='소속', widget=forms.TextInput(
        attrs={'class': 'form-control',}),
    )
    rank = forms.CharField(label='직위', widget=forms.TextInput(
        attrs={'class': 'form-control',}),
    )
    bachelor = forms.CharField(label='학사', widget=forms.TextInput(
        attrs={'class': 'form-control', }),
                           )
    master = forms.CharField(label='석사', widget=forms.TextInput(
        attrs={'class': 'form-control', }),
                           )
    doctor = forms.CharField(label='박사', widget=forms.TextInput(
        attrs={'class': 'form-control', }),
                           )

    is_admin = forms.BooleanField(label='관리자 유무', widget=forms.CheckboxInput(
        attrs={'class': 'form-control', }),
                             )

    is_out = forms.BooleanField(label='탈퇴 유무', widget=forms.CheckboxInput(
        attrs={'class': 'form-control', }),
                                  )

    class Meta:
        model = User()
        fields = ['name', 'phone', 'interest', 'belong', 'rank', 'bachelor', 'master', 'doctor', 'is_admin', 'is_out']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')


