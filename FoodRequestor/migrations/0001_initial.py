# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_name', models.CharField(max_length=50)),
                ('reg_email', models.EmailField(max_length=50)),
                ('reg_uid', models.CharField(max_length=20)),
                ('reg_pwd', models.CharField(max_length=20)),
                ('reg_contact_no', models.PositiveIntegerField(max_length=10)),
                ('reg_description', models.CharField(max_length=500)),
                ('reg_location', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
