# Generated by Django 3.0 on 2022-12-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('network', models.CharField(max_length=25, null=True)),
                ('relase_date', models.DateTimeField(null=True)),
                ('desc', models.TextField(null=True)),
            ],
        ),
    ]