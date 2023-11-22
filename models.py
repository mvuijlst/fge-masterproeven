from django.db import models

class Promotor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Thesis(models.Model):
    students = models.ManyToManyField(Student)
    promotor = models.ForeignKey(Promotor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    academic_year = models.CharField(max_length=9)
    title = models.TextField()
    summary = models.TextField()
    keywords = models.ManyToManyField(Keyword)

    def __str__(self):
        return self.title
