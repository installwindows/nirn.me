from django.db import models


class Nirn(models.Model):
    secret_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NirnFile(models.Model):
    nirn = models.ForeignKey(Nirn, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name
