# Generated by Django 2.1.7 on 2019-04-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190401_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionID', models.IntegerField()),
                ('question', models.TextField(max_length=200)),
                ('choiceA', models.TextField(max_length=200)),
                ('choiceB', models.TextField(max_length=200)),
                ('choiceC', models.TextField(max_length=200)),
                ('choiceD', models.TextField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
    ]
