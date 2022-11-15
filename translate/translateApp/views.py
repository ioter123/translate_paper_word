import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pathlib import Path
from .models import *
from . import papago_translate
from .token_word import filter_words
from .synonyms_find import synonyms
import math
import nltk
import tika
from tika import parser
import os, re
import pandas as pd
import numpy as np
import unicodedata
from nltk.tokenize import sent_tokenize
from nltk.data import load
import bcrypt
import jwt
from .tokens import account_activation_token
from .text import message
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from django.contrib import messages
from .decorators import *
from django.core.exceptions import PermissionDenied
from .forms import *
from django.views.generic import CreateView, FormView, ListView
from django.utils.decorators import method_decorator
from .helper import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.core.serializers.json import DjangoJSONEncoder
from .helper import email_auth_num
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.shortcuts import get_object_or_404
from datetime import datetime
EMAIL = getattr(settings, 'EMAIL', None)
SECRET_KEY = getattr(settings, 'SECRET_KEY', None)
nltk.download('punkt')


def main(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    return render(request, 'main.html', {'expiry_date' : expiry_date})


def guide(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    return render(request, 'guide.html', {'expiry_date' : expiry_date})


@login_message_required
def publicadministration(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    if request.method == 'POST':
        sentence_ids = request.POST.getlist('sentence_id')
        print(sentence_ids)
        for id in sentence_ids:
            print(id)
            try:
                error_sentence = request.POST[id]
                if error_sentence == 'True':
                    paperdb = PaperDB.objects.filter(id=int(id))
                    for paper in paperdb:
                        paper.error_sentence = True
                        paper.save()
            except:
                pass



        # 입력값
        startWord = request.POST['startWord']

        # 개행문자 제거
        new_startWord = startWord.replace('\r\n', '')

        # 입력값이 비어있는 경우
        if startWord=="":
            return render(request, 'publicadministration.html', {'startWord': new_startWord, 'transWord': "", 'tag1': "", 'expiry_date' : expiry_date})

        # 파파고 번역 실행
        #papago_word = papago_translate.papago_translate(new_startWord)

        # 번역이 안되는 경우
        #if not papago_word:
        #    return render(request, 'publicadministration.html', {'startWord': new_startWord, 'transWord': "", 'tag1': ""})

        # 파파고 번역어에 대한 특수문자 및 불용어 처리 및 형태소 분석
        #filtered_word = filter_words(papago_word)
        filtered_word = filter_words(startWord)

        # 파파고 변역어와 논문기반db 단어 매칭 - zeroWords : 해외논문사용x , transWords : 매칭으로 찾은 단어와 태그 및 빈도수
        transWords = []
        zeroWords = []
        for word in filtered_word:
            temp = list(PaperDB.objects.filter(sentence__icontains=word[0], error_sentence = False).values())
            if len(temp) != 0:
                temp.sort(key=lambda x : x['date'], reverse=True)
                transWords.append({'word': word[0], 'syn_word': '', 'count':len(temp), 'sentence':temp[:10], 'tag': word[1], 'syn_search':'no'})
            else:
                # 동의어 검색
                synonym_word = synonyms(word[0])
                synonym_trans = []
                for sy_word in synonym_word:
                    temp2 = list(PaperDB.objects.filter(sentence__icontains=sy_word).values())
                    if len(temp2) != 0:
                        synonym_trans.append({'word': word[0], 'syn_word': sy_word, 'count': len(temp2), 'sentence': temp2[:10], 'tag': word[1], 'syn_search':'yes'})
                if len(synonym_trans) == 0:
                    transWords.append({'word': word[0], 'syn_word': '', 'count': 0, 'sentence': '', 'tag': word[1], 'syn_search':'yes'})
                else:
                    synonym_trans.sort(key=lambda x: x['count'], reverse=True)
                    transWords.append(synonym_trans[0])

        # 빈도수별 정렬
        transWords.sort(key=lambda x : x['count'], reverse=True)

        tag1 = list(set([word['tag'] for word in transWords]))
        return render(request, 'publicadministration.html', {'startWord': new_startWord, 'transWords': transWords, 'tag1': tag1, 'expiry_date' : expiry_date})

    return render(request, 'publicadministration.html', {'startWord': "", 'transWord': "", 'tag1': "", 'expiry_date' : expiry_date})


def reload_paper(request):
    sentence_id = request.POST['sentence_id']

    paperdb = PaperDB.object.get(id=sentence_id)
    paperdb.error_sentence = error_sentence
    paperdb.save()
    return redirect('publicadministration')


def paperDBInsert(request):
    PaperDB.objects.all().delete()
    BASE_DIR = Path(__file__).resolve().parent.parent
    #print(BASE_DIR)
    path_dir = str(BASE_DIR)+'/sentence_jpart.xlsx'
    sentences = pd.read_excel(path_dir)

    for i in range(sentences.shape[0]):
        sentence = sentences.iloc[i,:]
        PaperDB.objects.create(
            id=i,
            depart=sentence['depart'],
            title=sentence['title'],
            author=sentence['author'],
            journal=sentence['journal'],
            date=sentence['date'],
            sentence=sentence['sentence'],
            search_cnt=sentence['search_cnt'],
        )
    print('done')
    return HttpResponse("success")


def research_part_insert(request):
    Researchpart.objects.all().delete()
    BASE_DIR = Path(__file__).resolve().parent.parent
    # print(BASE_DIR)
    path_dir = str(BASE_DIR) + '/연구분야 분류.xlsx'
    part = pd.read_excel(path_dir)

    for i in range(part.shape[0]):
        sentence = part.iloc[i, :]
        Researchpart.objects.create(
            part_1_code=sentence['최상위과학기술분류코드'],
            part_1_name=sentence['최상위과학기술분류코드한글명'],
            part_2_code=sentence['상위과학기술분류코드'],
            part_2_name=sentence['상위과학기술분류코드한글명'],
            code=sentence['과학기술분류코드'],
            name=sentence['연구분야'],
        )
    print('done')
    return HttpResponse("success")


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['part'] = list(Researchpart.objects.all().values())
        return context

    def get_success_url(self):
        self.request.session['register_auth'] = True
        messages.success(self.request, '회원님의 입력한 Email 주소로 인증 메일이 발송되었습니다. 인증 후 로그인이 가능합니다.')
        return reverse('register_success')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bachelor = '/'.join(self.request.POST.getlist('bachelor'))
        self.object.master = '/'.join(self.request.POST.getlist('master'))
        self.object.doctor = '/'.join(self.request.POST.getlist('doctor'))
        self.object.save()
        send_mail(
            '{}님의 회원가입 인증메일 입니다.'.format(self.object.name),
            [self.object.email],
            html=render_to_string('register_email.html', {
                'user': self.object,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)).encode().decode(),
                'domain': self.request.META['HTTP_HOST'],
                'token': default_token_generator.make_token(self.object),
            }),
        )

        return redirect(self.get_success_url())


def register_success(request):
    if not request.session.get('register_auth', False):
        raise PermissionDenied
    request.session['register_auth'] = False

    return render(request, 'register_success.html')


@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False

        return render(request, 'agreement.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True

            return redirect('/register/')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
            return render(request, 'agreement.html')


def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        current_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        messages.error(request, '메일 인증에 실패했습니다.')
        return redirect('user_login')

    if default_token_generator.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()

        messages.info(request, '메일 인증이 완료 되었습니다. 회원가입을 축하드립니다!')
        return redirect('user_login')

    messages.error(request, '메일 인증에 실패했습니다.')
    return redirect('user_login')


@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'user_login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            self.request.session['email'] = email
            login(self.request, user)
            remember_session = self.request.POST.get('remember_session', False)
            if remember_session:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/user_login')


@method_decorator(logout_message_required, name='dispatch')
class RecoveryIdView(View):
    template_name = 'recovery_id.html'
    recovery_id = RecoveryIdForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_id(None)
        return render(request, self.template_name, { 'form_id':form, })


def ajax_find_id_view(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    result_id = User.objects.get(name=name, phone=phone)

    return HttpResponse(json.dumps({"result_email": result_id.email}, cls=DjangoJSONEncoder),
                        content_type="application/json")


@method_decorator(logout_message_required, name='dispatch')
class RecoveryPwView(View):
    template_name = 'recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form_pw':form, })


def ajax_find_pw_view(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    target_user = User.objects.get(email=email, name=name, phone=phone)

    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num
        target_user.save()

        send_mail(
            '비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.email}, cls=DjangoJSONEncoder), content_type = "application/json")


def auth_confirm_view(request):
    email = request.POST.get('email')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(email=email, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.email

    return HttpResponse(json.dumps({"result": target_user.email}, cls=DjangoJSONEncoder),
                        content_type="application/json")


@logout_message_required
def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(email=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)

        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('user_login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'password_reset.html', {'form': reset_password_form})


@login_message_required
def profile_view(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    if request.method == 'GET':
        return render(request, 'profile.html', {'expiry_date' : expiry_date})


@login_message_required
def profile_update_view(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    if request.method == 'POST':
        request.user.bachelor = '/'.join(request.POST.getlist('bachelor1'))
        request.user.master = '/'.join(request.POST.getlist('master1'))
        request.user.doctor = '/'.join(request.POST.getlist('doctor1'))
        print(request.POST)
        print(request.user)
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            form = user_change_form.save(commit=True)
            form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('profile')
        return redirect('profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        part = Researchpart.objects.all()
        return render(request, 'profile_update.html', {'user_change_form':user_change_form, 'part': part.values(), 'expiry_date' : expiry_date})


@login_message_required
def password_edit_view(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('profile')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'profile_password.html', {'password_change_form':password_change_form, 'expiry_date' : expiry_date})


@login_message_required
def profile_delete_view(request):
    expiry_date = request.session.get_expiry_date()
    format = '%Y/%m/%d %H:%M:%S'
    expiry_date = expiry_date.strftime(format)
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/user_login/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'profile_delete.html', {'password_form': password_form, 'expiry_date' : expiry_date})


@method_decorator(admin_required, name='dispatch')
class UserListView(ListView):
    model = User
    paginate_by = 10
    template_name = 'user_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'user_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        user_list = User.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_user_list = user_list.filter(
                        Q(email__icontains=search_keyword) | Q(name__icontains=search_keyword) | Q(
                            phone__icontains=search_keyword))
                elif search_type == 'email_name':
                    search_user_list = user_list.filter(
                        Q(email__icontains=search_keyword) | Q(name__icontains=search_keyword))
                elif search_type == 'email':
                    search_user_list = user_list.filter(email__icontains=search_keyword)
                elif search_type == 'name':
                    search_user_list = user_list.filter(name__icontains=search_keyword)
                elif search_type == 'phone':
                    search_user_list = user_list.filter(phone__icontains=search_keyword)

                return search_user_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return user_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context


@admin_required
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'user_detail.html', context)


@admin_required
def user_edit_view(request, pk):
    user = User.objects.get(id=pk)

    if request.method == "POST":
        form = AdminUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "수정되었습니다.")
            return redirect('/user_list/' + str(pk))
    else:
        user = User.objects.get(id=pk)
        form = AdminUserChangeForm(instance=user)
        part = Researchpart.objects.all()
        context = {
            'user_change_form': form,
            'edit': '수정하기',
            'part': part.values()
        }
        return render(request, "user_edit.html", context)


@admin_required
def user_delete_view(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    messages.success(request, "삭제되었습니다.")
    return redirect('/user_list/')

