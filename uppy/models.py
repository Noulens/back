from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='treated')

    options = (
        ('ongoing', 'Ongoing'),
        ('treated', 'Treated'),
    )

    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100, null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pdf_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    status = models.CharField(max_length=10, choices=options, default='ongoing')
    objects = models.Manager()  # The default manager
    postobjects = PostObjects()  # The custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
