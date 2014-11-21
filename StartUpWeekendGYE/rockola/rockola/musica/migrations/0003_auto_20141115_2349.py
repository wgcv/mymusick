# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0002_cancion_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='musica',
            field=models.ForeignKey(to='musica.Musica', unique=True),
            preserve_default=True,
        ),
    ]
