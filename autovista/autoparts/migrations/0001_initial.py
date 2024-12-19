# Generated by Django 5.1.4 on 2024-12-18 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('model', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('discounted_price', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='auto_parts_images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_parts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
