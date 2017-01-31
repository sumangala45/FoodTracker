from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    reg_name = models.CharField(max_length=50)
    reg_email = models.EmailField(max_length=50)
    reg_uid = models.CharField(max_length=20)
    reg_pwd = models.CharField(max_length=20)
    reg_contact_no = models.PositiveIntegerField(max_length=10)
    reg_description = models.CharField(max_length=500)
    reg_location = models.CharField(max_length=255)

    def __str__(self):
        return self.reg_name

