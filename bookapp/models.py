from django.conf import settings
from django.db import models

from django.utils import timezone
from django.urls import reverse



# Create your models here.

BOOK_CATEGORY = (
    ('Arts & Music', 'Arts & Music'),
    ('Biographies', 'Biographies'),
    ('Business', 'Business'),
    ('Comics', 'Comics'),
    ('Computers & tech', 'Computers & tech'),
    ('Edu & Reference', 'Edu & Reference'),
    ('History', 'History'),
    ('Horror', 'Horror'),
    ('Mysterise', 'Mysterise'),
    ('Religion', 'Religion'),
    ('Romance', 'Romance'),
)


class Post(models.Model):
    author         = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category       = models.CharField(max_length=220, choices=BOOK_CATEGORY)
    integer        = models.IntegerField(blank=True,null=True)
    title          = models.CharField(max_length=200)
    text           = models.TextField()
    bookimg        = models.ImageField(blank=True)
    readpdf        = models.FileField(blank=True)
    audiofile       = models.FileField(blank=True)
    created_date   = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def get_absolute_url(self):
       return reverse("post_detail",kwargs={'pk':self.pk}) 


    def chart_data(self,User):
            list = Post.objects.all()
            return list

    def __str__(self):
        return self.title





class Comment(models.Model):
    post   =  models.ForeignKey('bookapp.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text   = models.TextField()
    create_date  = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text



