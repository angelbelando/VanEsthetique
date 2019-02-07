from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from django.utils import translation

class TranslatedField:
    def __init__(self, en_field, fr_field):
        self.en_field = en_field
        self.fr_field = fr_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'fr':
            return getattr(instance, self.fr_field)
        else:
            return getattr(instance, self.en_field)

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
    
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):
    date = models.DateField("Post date")
    intro_fr = models.CharField(max_length=255)
    intro_it = models.CharField(max_length=255)
    body_fr = RichTextField(blank=True)
    body_it = RichTextField(blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    intro = TranslatedField(
        'intro_it',
        'intro_fr',
    )

    body = TranslatedField(
        'body_it',
        'body_fr',
    )
    search_fields = Page.search_fields + [
        index.SearchField('intro_fr'),
        index.SearchField('body_fr'),
        index.SearchField('intro_it'),
        index.SearchField('body_it'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro_fr'),
        FieldPanel('intro_it'),
        # FieldPanel('intro'),
        FieldPanel('body_fr', classname="full"),
        FieldPanel('body_it', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]



