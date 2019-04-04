# Generated by Django 2.2 on 2019-04-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activities_sheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='projects.Project', verbose_name='project'),
        ),
    ]