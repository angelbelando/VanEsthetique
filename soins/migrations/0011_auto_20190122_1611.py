# Generated by Django 2.1.5 on 2019-01-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soins', '0010_family_care_name_it'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='care',
            options={'verbose_name': 'Soin', 'verbose_name_plural': 'Soins'},
        ),
        migrations.AlterModelOptions(
            name='family_care',
            options={'verbose_name': 'Famille de soin', 'verbose_name_plural': 'Familles de soin'},
        ),
        migrations.AddField(
            model_name='care',
            name='price_it',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=5, verbose_name='Prix Italien'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='care',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='nom du soin en Français'),
        ),
        migrations.AlterField(
            model_name='care',
            name='name_it',
            field=models.CharField(blank=True, max_length=64, verbose_name='nom du soin en Italien'),
        ),
        migrations.AlterField(
            model_name='care',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, verbose_name='Prix Français'),
        ),
        migrations.AlterField(
            model_name='family_care',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='nom en Français'),
        ),
        migrations.AlterField(
            model_name='family_care',
            name='name_it',
            field=models.CharField(blank=True, max_length=64, verbose_name='famille soin en Italien'),
        ),
    ]
