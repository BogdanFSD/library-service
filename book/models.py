from django.db import models


class Book(models.Model):
    COVER_CHOICES = (("HARD", "Hard Cover"), ("SOFT", "Soft Cover"))
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=4, choices=COVER_CHOICES, default="HARD")
    inventory = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.author}"
