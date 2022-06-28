import requests
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import User


def test1(request):
    email = EmailMessage('test','test', to=['lijahong111@gmail.com'])
    result = email.send()
    return HttpResponse()

def kakaologinpage(request):
    return render(request, 'login.html')

def getcode(request):
    code = request.GET.get('code')
    data = {'grant_type': 'authorization_code',
            'client_id':'569902a28ff22740161e573f603ec486', #발급받은 앱 키
            'redirect_uri': 'http://127.0.0.1:8000/oauth/redirect', #redirect url
            'code':code #받은 인가 코드
            }
    headers = {'Contents-type':'application/x-www-form-urlencoded;charset=utf-8'}
    res = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=headers) #import request해야한다, request package 설치 필요, res는 응답 받은 객체 이다
    token_json = res.json() #json 파일로 받아온다
    access_token = token_json['access_token'] #access_token 받아오기


    #token
    headers = {'Authorization': 'Bearer '+access_token,
               'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

    res = requests.get('https://kapi.kakao.com//v2/user/me', headers=headers)
    profile_res = res.json()

    nickname = profile_res['kakao_account']['profile']['nickname']
    print(nickname)
    kakaoid = profile_res['id']

    user = User.objects.filter(email=kakaoid)

    if user.first() is not None:
        login(request, user.first(), backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'profile.html')
    else :
        user = User()
        user.email = kakaoid #email란에 kakaoid를 넣어주겠다. email양식이 아니어도 가능하다
        user.username = nickname
        user.save()
        print('save it--------------------------')
        return render(request, 'login.html')



def profileshow(request):
    return render(request,'profile.html')



