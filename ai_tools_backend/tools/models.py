from django.db import models

# Create your models here.

class Tool(models.Model):
    CATEGORY_CHOICES = [
        ('Music', 'Music'),
        ('Video', 'Video'),
        ('Art', 'Art'),
        ('Code', 'Code'),
        ('Docs', 'Docs'),
        ('Study', 'Study'),
        ('Career', 'Career'),
        ('Present', 'Present'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('Analytics', 'Analytics'),
        ('Translate', 'Translate'),
        # Add more categories as needed
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='tool_images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    pricing = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
