from django.db import models


class Nirnroot(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    passphrase = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Nirn(models.Model):
    nirnroot = models.ForeignKey(Nirnroot, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    content = models.TextField(null=True, blank=True)
    json = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Nr[{self.nirnroot_id}] - {self.id}"


class NirnFile(models.Model):
    nirn = models.ForeignKey(Nirn, on_delete=models.CASCADE)
    file = models.FileField(upload_to='nirn_files/', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
