from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Pastry(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    image = models.ImageField(upload_to='pastries/', blank=True, null=True ,  default='images/default.jpg')
    difficulty_level = models.CharField(
        max_length=20,
        choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')],
        default='Easy'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pastry_detail', kwargs={'pk': self.pk})



class Recipe(models.Model):
    pastry = models.OneToOneField(Pastry, on_delete=models.CASCADE)
    ingredients = models.TextField()
    procedure = models.TextField()

    def __str__(self):
        return f"{self.pastry.name} Recipe"


class BakingTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='tips/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    pastry = models.ForeignKey(Pastry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username



class Rating(models.Model):
    pastry = models.ForeignKey(Pastry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)

    def __str__(self):
        return f"{self.score} stars for {self.pastry.name} by {self.user.username}"









