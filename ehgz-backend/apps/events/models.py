from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=100, null=True, blank=True)
    booked_by = models.ManyToManyField("accounts.User", blank=True, related_name='booked_events')
    description = models.TextField()
    description_ar = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
