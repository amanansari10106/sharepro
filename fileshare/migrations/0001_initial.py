# Generated by Django 3.2.4 on 2021-10-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]