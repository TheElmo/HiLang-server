# Generated by Django 2.0.5 on 2018-06-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_lesson_lessontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordlistquestion',
            name='sentenceStructure',
            field=models.BooleanField(default=False),
        ),
    ]
