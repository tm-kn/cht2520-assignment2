# Generated by Django 2.2 on 2019-04-04 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
        ('activities', '0002_translations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.AddField(
            model_name='activity',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', to='sheets.TimeSheet', verbose_name='time sheet'),
            preserve_default=False,
        ),
    ]