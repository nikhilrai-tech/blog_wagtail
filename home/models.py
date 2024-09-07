from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body=RichTextField(blank=True)

    content_panels=Page.content_panels+[
        FieldPanel("body")
    ]