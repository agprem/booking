from django.db import models

# Create your models here.
class advisor(models.Model):
    id = models.AutoField(primary_key=True,  editable=False)
    first_name=models.CharField(verbose_name="Advisor Name",max_length=25)
    profilepic=models.ImageField(upload_to="images/",null=True,blank=True)
    bookingtime=models.DateTimeField(blank=True,null=True)
    bookingid=models.IntegerField(blank=True,null=True)


