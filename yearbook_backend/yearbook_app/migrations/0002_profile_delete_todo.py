# Generated by Django 4.0.1 on 2022-02-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]