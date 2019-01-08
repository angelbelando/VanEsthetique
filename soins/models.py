from django.db import models
from django.utils.translation import ugettext_lazy as _

class Family_Care(models.Model):
    name = models.CharField(verbose_name=_('nom en Français'), max_length=64, unique=True)
    name_it = models.CharField(verbose_name=_('famille soin en Italien'), max_length=64, blank=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    display_order = models.IntegerField(verbose_name=_('ordre affichage'), blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Famille de soin'
        verbose_name_plural = 'Familles de soin'

class Care(models.Model):
    name = models.CharField(verbose_name=_('nom du soin en Français'), max_length=64, unique=True)
    name_it = models.CharField(verbose_name=_('nom du soin en Italien'), max_length=64, blank=True)
    family = models.ForeignKey(Family_Care, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_('Prix'), max_digits=5, decimal_places=0)
    display_order = models.IntegerField(verbose_name=_('ordre affichage'), blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Soin'
        verbose_name_plural = 'Soins'