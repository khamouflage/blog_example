# Generated by Django 4.1.3 on 2022-12-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publishedC', 'Published')], default='draft', max_length=10),
        ),
    ]
