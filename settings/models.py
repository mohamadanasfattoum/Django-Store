from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    call_as = models.CharField(max_length=20)
    email_as = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=300)
    emails = models.TextField(max_length=300)
    phones = models.TextField(max_length=300)
    address = models.TextField(max_length=300)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    yt_link = models.URLField(null=True, blank=True)
    app_description = models.CharField( max_length=300, null=True, blank=True)
    androud_app = models.URLField(null=True, blank=True)
    iphone_app = models.URLField(null=True, blank=True)



    def __str__(self) -> str:
        return self.name
