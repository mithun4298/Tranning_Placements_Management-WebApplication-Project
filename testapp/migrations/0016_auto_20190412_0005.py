# Generated by Django 2.2 on 2019-04-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20190325_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_resume1',
            field=models.FileField(default='resume/CRT.pdf', upload_to='resume/%Y/%m/%D'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_resume2',
            field=models.FileField(default='resume/CRT.pdf', upload_to='resume/%Y/%m/%D'),
        ),
    ]