# Generated by Django 4.0 on 2021-12-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
