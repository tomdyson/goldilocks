from django.db import models
from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


@register_setting
class LinkSettings(BaseSetting):

    about_page = models.ForeignKey(
        "wagtailcore.Page", null=True, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        PageChooserPanel("about_page"),
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    body = StreamField(
        [
            ("heading", blocks.CharBlock(classname="full title", icon="title")),
            (
                "paragraph",
                blocks.RichTextBlock(
                    icon="pilcrow", features=["bold", "italic", "link"]
                ),
            ),
            ("image", ImageChooserBlock(icon="image")),
            ("embed", EmbedBlock(icon="media")),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        StreamFieldPanel("body"),
    ]

    api_fields = [APIField("date"), APIField("body")]
