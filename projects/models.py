from django.db import models
from cloudinary.models import CloudinaryField
from skills.models import Skills

# Create your models here.
class Project(models.Model):
    ITEM_TYPES = [
        ('projects', 'Projects'),
    ]
    title = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, null=True)
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE,related_name='projects',null=True)
    description = models.TextField(null=True, blank=True)
    image= models.ImageField('projects',default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqrKzwI1LUg0ORMtSvgvjRjgHdTzAIu_rf2g&s')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
