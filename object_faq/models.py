"""Models of the object_faq app."""
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from hvad.models import TranslatableModel, TranslatedFields


class Entry(TranslatableModel):
    """
    Holds the questions and answers for a related object.

    :object: GFK to the object.
    :position: Positive integer for the position of this object.

    translated:
    :answer: The answer to the question.
    :question: The question about this object.

    """
    object = generic.GenericForeignKey()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(null=True, blank=True)

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        blank=True, null=True,
    )

    translations = TranslatedFields(
        answer=models.TextField(
            verbose_name=_('Answer'),
            blank=True,
        ),
        question=models.CharField(
            verbose_name=_('Question'),
            max_length=256,
        ),
    )

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        title = self.safe_translation_getter(
            'question', 'Question {0}'.format(self.pk))
        return '{0} - {1}'.format(title, self.object)


class GlobalObjectDescription(TranslatableModel):
    """
    Model for storing optional descriptions for the rendered faq or object.

    You can use this e.g. for a general introduction and title for the faq.

    :object: GFK to the object.

    translated:
    :content: The text, that should be displayed.
    :title: The optional title of this description.

    """
    object = generic.GenericForeignKey()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(null=True, blank=True)

    translations = TranslatedFields(
        content=models.TextField(
            verbose_name=_('Content'),
        ),
        title=models.CharField(
            verbose_name=_('Title'),
            max_length=256,
            blank=True,
        ),
    )

    class Meta:
        unique_together = ['content_type', 'object_id']

    def __unicode__(self):
        title = self.safe_translation_getter(
            'title', 'Title {0}'.format(self.pk))
        return '{0} for {1}'.format(title, self.object)
