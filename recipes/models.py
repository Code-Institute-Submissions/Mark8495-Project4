from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))



class Preptime(models.Model):
    "Django Model of Preparation time database"
    preptime_image = CloudinaryField("preptime", blank=True)
    title = models.CharField(max_length=250, default='placeholder', unique=True, null=True)
    slug = models.SlugField(max_length=250, default='placeholder', unique=True, null=True)

    class Meta:
        verbose_name_plural = 'preptimes'

    def __str__(self):
        return self.title


class Mealtime(models.Model):
    "Django Model of Preparation time database"
    title = models.CharField(max_length=250, default='breakfast', unique=True, null=True)
    slug = models.SlugField(max_length=250, default='breakfast', unique=True, null=True)
    mealtime_image = CloudinaryField("mealtime", blank=True)

    class Meta:
        verbose_name_plural = 'mealtimes'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    " Django Model of recipe database "
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    preptime = models.ForeignKey(
        Preptime,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    mealtime = models.ForeignKey(
        Mealtime,
        on_delete=models.CASCADE,
        related_name="recipe_posts"
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="recipe_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    serving_size = models.CharField(max_length=30, default=0)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, 
        related_name='recipe_likes', 
        blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    "Comments Model"
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"