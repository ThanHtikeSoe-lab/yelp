from django.db import models

# Create your models here.
class Business(models.Model):
        id=models.CharField(primary_key=True,max_length=100)
        name=models.CharField(max_length=100)
        address=models.CharField(max_length=100,null=True)
        city=models.CharField(max_length=100)
        state=models.CharField(max_length=100)
        stars=models.FloatField()
        categories=models.TextField(null=True)

        def __str__(self):
            return self.name
        
class User(models.Model):
      id=models.CharField(primary_key=True,max_length=100)
      name=models.CharField(max_length=100)
      yelping_since=models.DateTimeField()

      def __str__(self):
            return self.name
status_choice=(('approved','APPROVED'),('pending','PENDING'),
               ('rejected','REJECTED'))

class Review(models.Model):
      id=models.CharField(primary_key=True,max_length=100)
      status=models.CharField(max_length=10,choices=status_choice,default='pending')
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      stars=models.IntegerField()
      text=models.TextField()
      date=models.DateTimeField()

      
      def __str__(self):
         return self.name