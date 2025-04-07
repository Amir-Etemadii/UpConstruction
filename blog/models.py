from django.db import models
from account.models import CustomUser
from blog.managers import ActivePostManager

class Category(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def create_format(self):
        return self.created_at.strftime('%Y-%m-%d')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/post', null=True, blank=True)

    objects= models.Manager()
    active_objects = ActivePostManager()

    def create_format_short(self):
        return self.created_at.strftime("%B %d")

    def create_format_long(self):
        return self.created_at.strftime("%b %d, %Y")

    def save(self, *args, **kwargs):
        self.title= self.title.title()
        super(Post, self).save(args, kwargs)

    def __str__(self):
        return f'{self.title}--{self.content[:10]}'


