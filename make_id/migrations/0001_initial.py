# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('uid', models.CharField(max_length=30)),
                ('reference_type', models.CharField(max_length=30)),
                ('origin', models.CharField(max_length=30, default='tgac')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
