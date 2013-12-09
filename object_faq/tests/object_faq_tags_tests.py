"""Tests for the template tags of the object_faq app."""
from django.test import TestCase

from django_libs.tests.factories import UserFactory

from ..templatetags.object_faq_tags import render_faq_for_object
from .factories import EntryFactory


class RenderFAQForObjectTestCase(TestCase):
    """Test case for the ``render_faq_for_object`` template tag."""
    longMessage = True

    def setUp(self):
        self.user = UserFactory()
        self.entry = EntryFactory(object=self.user)

    def test_tag(self):
        self.assertEqual(
            render_faq_for_object({}, self.user)['faqs'][0], self.entry)
