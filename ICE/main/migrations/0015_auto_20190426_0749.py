# Generated by Django 2.1.7 on 2019-04-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_category_component_courset_history_instructor_instructorinfo_learner_module_modulet_progress_questio'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='place',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='component',
            name='title',
            field=models.CharField(default='entry', max_length=200),
        ),
    ]