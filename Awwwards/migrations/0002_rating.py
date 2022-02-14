# Generated by Django 4.0.1 on 2022-02-14 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Awwwards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2200, verbose_name='Comment')),
                ('design_rating', models.IntegerField(default=0)),
                ('usability_rating', models.IntegerField(default=0)),
                ('content_rating', models.IntegerField(default=0)),
                ('creativity_rating', models.IntegerField(default=0)),
                ('experience_rating', models.IntegerField(default=0)),
                ('avarage_rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Awwwards.portfolio')),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]