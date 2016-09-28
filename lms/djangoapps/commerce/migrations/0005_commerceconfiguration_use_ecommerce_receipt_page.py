# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20160531_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='commerceconfiguration',
            name='use_ecommerce_receipt_page',
            field=models.BooleanField(default=False, help_text='Use the receipt page hosted by the E-Commerce service.'),
        ),
    ]
