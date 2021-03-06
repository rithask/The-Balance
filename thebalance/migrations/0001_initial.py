# Generated by Django 4.0.1 on 2022-01-29 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_items', to='thebalance.date')),
            ],
        ),
    ]
