from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from uppy.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):

    def test_view_post(self):
        url = reverse('uppy_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456')

        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse('uppy_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456')
        self.client.login(username=self.testuser1.username, password='123456')
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse('uppy_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456')
        self.testuser2 = User.objects.create_user(username='test_user2', password='123456')
        test_post = Post.objects.create(title='Post Title', excerpt='Post Excerpt',
                                        content='Post Content', author=1, status='published', category_id=1)
        client.login(username=self.testuser1.username, password='123456')

        url = reverse('uppy_api:detailcreate', kwargs={'pk': 1})

        response = client.put(url, {
            "title": "new",
            "author": 1,
            "excerpt": "new",
            "content": "new",
            "status": "published"
        }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
