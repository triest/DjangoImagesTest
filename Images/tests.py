from django.test import TestCase
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Image, Comment


# Create your tests here.
class ImagesTestCase(TestCase):
    def setUp(self):
        self.lion = Image.objects.create(title="lion")

    def test_was_published_recently_with_future_question(self):
        self.assertEqual(self.lion.title, 'lion')
        #  self.assertEquals(self.lion.date,'')


class CommentsTestCase(TestCase):
    def setUp(self):
        self.image = Image.objects.create(title="lion")
        self.comment = Comment.objects.create(title="Test title", image=self.image)

    def test_create_comment(self):
        self.assertEquals(self.comment.title, "Test title")
        self.assertEquals(self.comment.image, self.image)

    def test_delete_comment(self):
        self.comment.delete();
        self.assertTrue(self.comment is not None)
