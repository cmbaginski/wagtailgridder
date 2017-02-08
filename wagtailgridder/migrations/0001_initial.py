# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GridCategoryGridItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailgridder.GridCategory')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GridIndexGridItemRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GridIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Grid Index Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GridItem',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('summary', wagtail.wagtailcore.fields.RichTextField(default='', help_text='The summary will appear in the item "card" view.', verbose_name='Summary')),
                ('full_desc', wagtail.wagtailcore.fields.RichTextField(default='', help_text='The description will appear when the grid item is clicked and expanded.', verbose_name='Full Description')),
                ('target_url', models.URLField(blank=True, default='', help_text='The URL for this grid item, if it is not a full Django App.', verbose_name='URL')),
                ('modified', models.DateTimeField(null=True, verbose_name='Page Modified')),
                ('buttons', wagtail.wagtailcore.fields.StreamField((('button_section', wagtail.wagtailcore.blocks.StructBlock((('action_items', wagtail.wagtailcore.blocks.StreamBlock((('document_button', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=True))), icon='fa-file')), ('url_button', wagtail.wagtailcore.blocks.StructBlock((('label', wagtail.wagtailcore.blocks.TextBlock(required=True)), ('url', wagtail.wagtailcore.blocks.URLBlock(required=True))), icon='fa-link')), ('placeholder', wagtail.wagtailcore.blocks.StructBlock((), icon='fa-square-o'))), help_text='A button or URL within a button section.')),))),), null=True)),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('small_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Grid Item',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GridItemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='wagtailgridder.GridItem')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wagtailgridder_griditemtag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='griditem',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='wagtailgridder.GridItemTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='gridindexgriditemrelationship',
            name='GridRelationship',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='grid_index_grid_item_relationship', to='wagtailgridder.GridIndexPage'),
        ),
        migrations.AddField(
            model_name='gridindexgriditemrelationship',
            name='grid_item',
            field=models.ForeignKey(help_text='Add a grid item to the page', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailgridder.GridItem', verbose_name='Grid Items'),
        ),
        migrations.AddField(
            model_name='gridcategorygriditem',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='wagtailgridder.GridItem'),
        ),
    ]
