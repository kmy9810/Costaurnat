from django.db import models
#데이터 베이스 연동

class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    