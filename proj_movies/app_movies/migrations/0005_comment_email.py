# Generated by Django 4.1 on 2022-09-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_movies', '0004_alter_person_birth_alter_person_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='admin@admin.ru', max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
    ]
