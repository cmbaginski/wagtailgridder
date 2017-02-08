# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 14:19
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailgridder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='griditem',
            name='landing_page_text',
            field=wagtail.wagtailcore.fields.RichTextField(default='', help_text="This is the text which will appear on the grid item's landing page.", verbose_name='Landing Page Text'),
        ),
    ]
