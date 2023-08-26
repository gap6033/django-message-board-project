from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='A test post')

    def test_post_text_content(self):
        post = Post.objects.get(id=1)
        returned_text = post.text[:50]
        self.assertEqual(returned_text, 'A test post')

class HomePageViewTest(TestCase):
    def test_home_page_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_access_via_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_right_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')