# Generated by Django 4.1.5 on 2023-12-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]