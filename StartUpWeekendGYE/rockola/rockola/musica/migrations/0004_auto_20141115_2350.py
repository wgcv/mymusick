# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_auto_20141115_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='musica',
            field=models.ForeignKey(to='musica.Musica'),
            preserve_default=True,
        ),
    ]
