from django.db import models


class Double(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    double_value = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
