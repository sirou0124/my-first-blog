# Generated by Django 2.0.6 on 2019-07-30 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='appoved_comment',
            new_name='approved_comment',
        ),
    ]
