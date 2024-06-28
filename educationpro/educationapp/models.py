from django.db import models

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    studentsenrolled=models.FloatField(default=0.0)
    updatedon=models.CharField(max_length=50)
    course_image=models.ImageField(null=True,blank=True,upload_to="images/")


class Customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    emailId=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)

class CartModel(models.Model):
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)
    emailId=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # quantity=models.IntegerField()
    totalPrice=models.FloatField(default=0.0)


class Orders(models.Model):
    orderId=models.AutoField(primary_key=True)
    emailId=models.CharField(max_length=100)
    ordernumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    phoneno=models.IntegerField()
    totalbillamount=models.FloatField(default=0.0)

class Payment(models.Model):
    emailId=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_st=models.DateTimeField(auto_now=True)

class Payment(models.Model):
    emailId=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_st=models.DateTimeField(auto_now=True)
