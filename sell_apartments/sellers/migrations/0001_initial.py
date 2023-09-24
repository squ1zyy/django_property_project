# Generated by Django 4.2.4 on 2023-09-15 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PictureMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_estate', models.CharField(choices=[('apartment', 'Apartment'), ('house', 'House')], default='apartment', max_length=10)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('price', models.IntegerField(null=True)),
                ('amount_rooms', models.IntegerField(null=True)),
                ('pictures', models.ManyToManyField(blank=True, related_name='Estate', to='sellers.picturemain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='picturemain',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.realestate'),
        ),
    ]
