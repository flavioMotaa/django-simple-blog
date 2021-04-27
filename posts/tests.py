from django.test import TestCase
from django.db import models
from django.utils import timezone
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
    def createTestPost(self, topic="testTopic", title="something"):
        return Post.objects.create(topic=topic, title=title, created_at=timezone.now())

    def test_savePost(self):
        postToBeSaved = self.createTestPost()
        self.assertEqual(postToBeSaved.save(), postToBeSaved) #Isso tem que dar erro
    def test_IfPostCreated(self):
        created_post = self.createTestPost()
        self.assertTrue(isinstance(created_post, Post))
        self.assertEqual(created_post.__str__(), created_post.title)
