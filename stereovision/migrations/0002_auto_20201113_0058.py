# Generated by Django 3.1.2 on 2020-11-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stereovision', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='left_camera',
            new_name='user_left_camera',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='right_camera',
            new_name='user_right_camera',
        ),
    ]
