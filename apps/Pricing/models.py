from django.db import models
from apps.Package.models import Package

class Pricing(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    pp_in_dbl = models.FloatField(verbose_name="Price Per Person in Double")
    pp_in_sgl = models.FloatField(verbose_name="Price Per Person in Single")
    chd_2_6 = models.FloatField(verbose_name="Child 2-6 Years Rate")
    chd_6_11 = models.FloatField(verbose_name="Child 6-11 Years Rate")
    infant_rate = models.FloatField(verbose_name="Infant Rate")

    def __str__(self):
        return f"Pricing for {self.package}" 