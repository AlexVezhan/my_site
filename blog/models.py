
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'

class Author(models.Model):
    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f'{self.firts_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=150, blank=True)
    excerpt = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to = 'posts', null = True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

