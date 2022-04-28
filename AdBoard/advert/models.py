from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    Tanks = 'TNK'
    Healers = 'HLR'
    DD = 'DD'
    Merchants = 'MRH'
    GuildMasters = 'GUI'
    QuestGivers = 'QST'
    Blacksmiths = 'BSM'
    Tanners = 'TNR'
    PotionMakers = 'PON'
    SpellMasters = 'SPL'

    CATEGORY = [(Tanks, 'Танки'),
                (Healers, 'Хилы'),
                (DD, 'ДД'),
                (Merchants, 'Торговцы'),
                (GuildMasters, 'Гилдмастеры'),
                (QuestGivers, 'Квестгиверы'),
                (Blacksmiths, 'Кузнецы'),
                (Tanners, 'Кожевники'),
                (PotionMakers, 'Зельевары'),
                (SpellMasters, 'Мастеразаклинаний'),
                ]
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Ad(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="copyright")
    ad_time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    text = RichTextUploadingField()

    def preview(self):
        return f'{self.text[0:123]} ...'

    def __str__(self):
        return f'{self.headline}{self.ad_time_in}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return reverse('adsdetail', kwargs={'pk': self.pk})


class Response(models.Model):
    resp_post = models.ForeignKey(Ad, on_delete=models.CASCADE)
    resp_user = models.ForeignKey(User, on_delete=models.CASCADE)
    resp_text = models.TextField()
    resp_time_in = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def accept_comment(self):
        self.accepted = True
        self.save()

    def __str__(self):
        return f'{self.reso_text[0:20]}'


class AdResponse(models.Model):
    Ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __str__(self):
    #    return f'{self.category.title()}'


class AdCategory(models.Model):
    ad_ref = models.ForeignKey("Ad", on_delete=models.CASCADE)
    ad_category = models.ForeignKey("Category", on_delete=models.CASCADE)
