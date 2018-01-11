# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-09 13:25
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion

from module.models import CollectionGroup

def migrate_data_forward(apps, schema_editor):
    for instance in CollectionGroup.objects.all():
        print "Generating slug for %s" % instance
        instance.save() # Will trigger slug update

def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0003_auto_20171215_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectiongroup',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from=b'name', unique_with=[b'owner']),
        ),
        migrations.AddField(
            model_name='engine',
            name='host',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='engine',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sequence',
            name='engine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module.Engine'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='correctness_matters',
            field=models.BooleanField(default=True, help_text=b'If checked: grade will depend on points user get,<br>If unchecked: grade will depend on users trials count.', verbose_name=b'Correctness matters (grading policy setting)'),
        ),
        migrations.AlterUniqueTogether(
            name='engine',
            unique_together=set([('host', 'token')]),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
    ]
