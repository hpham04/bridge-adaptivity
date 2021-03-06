# Generated by Django 2.0.5 on 2018-06-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_oauthclient_content_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauthclient',
            name='grant_type',
            field=models.CharField(blank=True, choices=[('code', 'authorization code'), ('implicit', 'implicit'), ('password', 'resource owner password-based'), ('credentials', 'client credentials')], default='credentials', help_text='OAuth grant type which is used by OpenEdx API.', max_length=255, null=True),
        ),
    ]
