# Generated by Django 3.2.9 on 2021-11-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('anc_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
