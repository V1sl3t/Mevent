# Generated by Django 4.2.3 on 2024-05-29 13:49

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_remove_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('city_name', models.CharField(max_length=50)),
                ('place_id', models.CharField(default='ChIJ02oeW9PP20YR2XC13VO4YQs', max_length=256)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(27.561831, 53.902284), srid=4326)),
                ('city_south_west_point', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(27.38909, 53.82427), srid=4326)),
                ('city_north_east_point', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(27.76125, 53.978), srid=4326)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
            },
        ),
    ]
