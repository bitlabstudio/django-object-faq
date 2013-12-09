"""Tests for the models of the object_faq app."""
from django.test import TestCase

from .factories import EntryFactory, GlobalObjectDescriptionFactory


class EntryTestCase(TestCase):
    """Tests for the ``Entry`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``Entry`` model."""
        entry = EntryFactory()
        self.assertTrue(entry.pk)


class GlobalObjectDescriptionTestCase(TestCase):
    """Tests for the ``GlobalObjectDescription`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``GlobalObjectDescription`` model."""
        globalobjectdescription = GlobalObjectDescriptionFactory()
        self.assertTrue(globalobjectdescription.pk)
