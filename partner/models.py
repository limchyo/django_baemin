from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Partner(models.Model):
    KOREAN = 'ko'
    JAPANESE = 'jp'
    CHINESE = 'cn'
    ITALIAN = 'it'
    FOOD_CHOICES = (
        (KOREAN, 'Korean'),
        (JAPANESE, 'Japanese'),
        (CHINESE, 'Chinese'),
        (ITALIAN, 'Italian'),
    )
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
    category = models.CharField(
        max_length=2,
        choices=FOOD_CHOICES,
        default=KOREAN,
    )

    def __str__(self):
        return self.name

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

    def __str__(self):
        return ("{}({})").format(self.name, self.partner.name)
