from django.test import TestCase

# Create your tests here.
from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='just a test')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'just a test')