from django.contrib.auth.base_user import AbstractBaseUser #model, 인증 방식까지 다 사용자 맞춤으로 설정
from django.contrib.auth.models import AbstractUser #model만 수정, 기능은 가져와서 쓴다
from django.db import models

class User(AbstractUser) :
    pass


