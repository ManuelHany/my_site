from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)           # very short text.

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100) # EmailField is better than the charfield because it validates the e-mail.

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)       # later on it can be image uploads.
    date = models.DateField(auto_now=True)              # so when I save it it sets it with the  current date
    slug = models.SlugField(unique=True)                # unique as it will  be the unique identifier for my posts endpoints
                                                        # 2 reasons why we ommit the db_index=True field:
                                                        # a -> slugfield has default value for db_index=True
                                                        # b -> unique=True implies also that db_index=True
    content = models.TextField(MinLengthValidator(500))  # Textfield is a large field for text data.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
                                                        # ForeignKey is always added in the many side.
                                                        # as it is a one to many relation, the related_name is usefule,
                                                        # when accessing the field from the "one" side of the relation
                                                        # using the reverse method.
    tags = models.ManyToManyField(Tag, null=True)       # where to put the ManyToMany relation depends on your common sense.


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    
