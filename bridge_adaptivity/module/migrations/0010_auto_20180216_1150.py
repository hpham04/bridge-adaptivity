# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-16 11:50
from __future__ import unicode_literals

import sys
import uuid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def forward_function(apps, schema):
    """Remove all data from module app.
    migrations.RunPython(forward_function, lambda *a, **kw: None),
    """
    sql_template = """
    BEGIN;
    TRUNCATE {tables};
    {reset_ids}
    COMMIT;
    """
    all_tables = [
        "bridge_lti_ltiuser","bridge_lti_outcomeservice", "bridge_lti_lticonsumer", "bridge_lti_bridgeuser_groups",
        "bridge_lti_bridgeuser", "bridge_lti_bridgeuser_user_permissions", "bridge_lti_ltiprovider",
        "module_sequence", "module_engine", "module_log", "module_collection",
        "module_collectiongroup",
        "module_collectiongroup_collections", "module_gradingpolicy", "module_sequenceitem", "module_activity"
    ]
    reset_tables = [t for t in all_tables if 'module_' in t]
    reset_ids = "\n".join(
        """SELECT setval(pg_get_serial_sequence('"{}"','id'), 1, false);""".format(table)
        for table in reset_tables
    )
    sql = sql_template.format(
        tables=', '.join('"{}"'.format(i) for i in reset_tables),
        reset_ids=reset_ids
    )
    prompt = """\n\n\nThis migration will remove ALL data from `module` application!!!
\nAre you sure that you want to proceed?
Type: yes/no\n"""
    if len(sys.argv) > 1:
        return
        cursor = schema.connection.cursor()
        cursor.execute(sql)
        print "Data removed and migration process will be continued.\n"
    else:
        print "Dump data, write script to migrate data and run migration process again and answer YES.\n"


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module', '0009_auto_20180207_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(forward_function, lambda *a, **kw: None),
        migrations.AlterField(
            model_name='collectiongroup',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='collectiongroup',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_groups', to='module.Course'),
        ),
        migrations.AlterField(
            model_name='collectiongroup',
            name='collections',
            field=models.ManyToManyField(blank=True, related_name='collection_groups', to='module.Collection'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='tags',
            field=models.CharField(blank=True, help_text=b'Provide your tags separated by a comma.', max_length=255, null=True),
        ),
    ]