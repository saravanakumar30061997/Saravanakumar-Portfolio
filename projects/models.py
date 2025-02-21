from django.db import models

# Create your models here.
class Project(models.Model):
    ITEM_TYPES = [
        ('projects', 'Projects'),
    ]
    title = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
