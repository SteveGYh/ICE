# Generated by Django 2.1.7 on 2019-04-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_merge_20190416_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateID', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('contain_course', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstructorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructorID', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('intro', models.TextField(max_length=200)),
            ],
        ),
    ]