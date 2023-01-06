# Generated by Django 4.1.5 on 2023-01-06 17:32

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_remove_linksettings_site_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            form_classname="full title", icon="title"
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(
                            features=["bold", "italic", "link"], icon="pilcrow"
                        ),
                    ),
                    ("image", wagtail.images.blocks.ImageChooserBlock(icon="image")),
                    ("embed", wagtail.embeds.blocks.EmbedBlock(icon="media")),
                ],
                use_json_field=True,
            ),
        ),
    ]
