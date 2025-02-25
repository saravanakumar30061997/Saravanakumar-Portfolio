from django.db import models
from cloudinary.models import CloudinaryField
from skills.models import Skills

# Create your models here.
class PortfolioItem(models.Model):
    ITEM_TYPES = [
        ('certification', 'Certification'),
    ]
    title = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES, null=True)
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE,related_name='certifications',null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField('Portfolio', null= True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
