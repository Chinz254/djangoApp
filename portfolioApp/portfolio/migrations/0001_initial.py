# Generated by Django 2.0.6 on 2018-06-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_description', models.CharField(blank=True, max_length=100, null=True)),
                ('details', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('finished_date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='media')),
                ('project_files', models.ImageField(blank=True, null=True, upload_to='media')),
                ('cliente', models.CharField(blank=True, default='Personal Project', max_length=100, null=True)),
            ],
        ),
    ]
