from django.db import models

# Create your models here.
class Date(models.Model):
    date = models.DateField(primary_key=True)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

class Shopping(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    price = models.FloatField()
    # category = models.CharField(max_length=200)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, related_name='bought_items')
    
    def __str__(self):
        return f"{self.item} - {self.price} - {self.date}"