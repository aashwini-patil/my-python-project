from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    content = models.TextField()

    def summary(self):
        return self.content[:100]
    
    def pub_date(self):
        return self.pub_date.strftime('%b %e, %y')
    
    def __str__(self):
        return self.title