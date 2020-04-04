from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    creator = models.CharField(max_length=2000)
    paradigm = models.CharField(max_length=2000)
    last_paradigm = models.CharField(max_length=2000, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
