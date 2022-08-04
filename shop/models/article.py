from django.db import models


class Article(models.Model):
    title = models.CharField(("Article title"), max_length=200, null=False, default="null")
    synopsis = models.CharField(("Article synopsis"), max_length=312, null=True, default="null")
    img = models.ImageField(null=False)
    url = models.CharField(("Article URL"), null=True, default="#", max_length=200)
    created = models.DateTimeField(("Article Created"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)
