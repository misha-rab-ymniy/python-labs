# Generated by Django 4.2.1 on 2023-09-23 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film', to='cinema.film'),
        ),
    ]