# Generated by Django 2.0.6 on 2018-07-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0005_merge_20180725_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='example_sentence',
            field=models.TextField(default='', help_text='An example sentence in the to language'),
            preserve_default=False,
        ),
    ]
