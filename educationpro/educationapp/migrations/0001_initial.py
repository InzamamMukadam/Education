# Generated by Django 5.0.6 on 2024-05-30 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0.0)),
                ('studentsenrolled', models.FloatField(default=0.0)),
                ('updatedon', models.CharField(max_length=50)),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('emailId', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('emailId', models.CharField(max_length=100)),
                ('ordernumber', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('phoneno', models.IntegerField()),
                ('totalbillamount', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailId', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('amount_paid', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_st', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalPrice', models.FloatField(default=0.0)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educationapp.course')),
                ('emailId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educationapp.customer')),
            ],
        ),
    ]
