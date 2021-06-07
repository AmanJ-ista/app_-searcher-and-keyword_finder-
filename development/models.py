from django.db import models

class first_url(models.Model):
    keywords_url=models.CharField(max_length=200)
    description_url=models.CharField(max_length=200)
    ogdescription_url=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='first_url'
