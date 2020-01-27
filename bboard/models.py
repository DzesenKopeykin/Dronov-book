from django.db import models


class BillBoard(models.Model):
    title = models.CharField(max_length=50, verbose_name="Product")
    content = models.TextField(null=True, blank=True, verbose_name="Description")
    price = models.FloatField(null=True, blank=True, verbose_name="Price")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="published")

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
        ordering = ["-published"]
