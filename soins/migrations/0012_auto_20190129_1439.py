# Generated by Django 2.1.5 on 2019-01-29 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soins', '0011_auto_20190122_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='care',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soins.Family_Care', verbose_name='Famille de soins'),
        ),
    ]
