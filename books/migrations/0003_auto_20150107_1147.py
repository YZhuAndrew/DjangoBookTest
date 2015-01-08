# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150107_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
