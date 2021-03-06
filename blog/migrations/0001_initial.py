# Generated by Django 3.2.9 on 2021-11-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_dt', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]
