from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        verbose_name="업체명"
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="업체 연락처"
    )
    address = models.CharField(
        max_length=200,
        verbose_name="업체 주소"
    )
    description = models.TextField(
        verbose_name="업체 소개"
    )

class Menu(models.Model):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name="메뉴이미지"
    )
    name = models.CharField(
        max_length=50,
        verbose_name="메뉴명"
    )
    price = models.PositiveIntegerField(
        verbose_name="가격"
    )
