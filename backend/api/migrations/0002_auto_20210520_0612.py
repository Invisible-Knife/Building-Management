# Generated by Django 3.2.3 on 2021-05-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='code',
        ),
        migrations.RemoveField(
            model_name='human',
            name='guest_can_pause',
        ),
        migrations.RemoveField(
            model_name='human',
            name='host',
        ),
        migrations.RemoveField(
            model_name='human',
            name='votes_to_skip',
        ),
        migrations.AddField(
            model_name='human',
            name='company',
            field=models.CharField(default='none', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='human',
            name='name',
            field=models.CharField(default='Guest', max_length=50),
        ),
    ]