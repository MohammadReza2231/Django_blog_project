from ast import arg

from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='post1',
            text='this is a test',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )

        cls.post2 = Post.objects.create(
            title='postTest2',
            text='lorem ipsom post3',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post1')
        self.assertEqual(self.post1.text, 'this is a test')

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_draft__post_not_show(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'some titile',
            'text': 'this is a test',
            'status': 'pub',
            'author': self.user.id,

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some titile')
        self.assertEqual(Post.objects.last().text, 'this is a test')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'post2 update',
            'text': 'this text is update',
            'status': 'pub',
            'author': self.post2.author.id,

        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post2 update')
        self.assertEqual(Post.objects.last().text, 'this text is update')

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
