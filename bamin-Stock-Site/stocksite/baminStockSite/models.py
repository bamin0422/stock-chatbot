from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        abstract = True

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class StockCommunity(Post):

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def getName(self):
        return "토론실"

    def __str__(self):
        return self.title


class StockNews(Post):

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def getName(self):
        return "주요공시"

    def __str__(self):
        return self.title


class SpecialStock(Post):

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def getName(self):
        return "특징주"

    def __str__(self):
        return self.title
