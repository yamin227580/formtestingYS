# Generated by Django 2.0 on 2020-10-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_post_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='GModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('G_mail', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]