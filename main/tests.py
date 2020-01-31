from django.test import TestCase, Client
import json
import pdb

from .models import *

def dummy_user(id):
    user_data = {
            'username': 'test_user_%d' % id,
            'email': 'test@test.com',
            'password':'test'
            }
    return User.objects.create_user(
            username = user_data['username'],
            email = user_data['email'],
            password = user_data['password']
            )

def dummy_post():
    post_data = {
            'title': 'test title',
            'content': 'test content',
            'author': dummy_user(10).profile
            }
    return Post.objects.create(
            title = post_data['title'],
            content = post_data['content'],
            author = post_data['author']
            )

def dummy_comment():
    comment_data = {
            'content': 'test content',
            'author': dummy_user(20).profile,
            'post': dummy_post()
            }
    return Comment.objects.create(
            content = comment_data['content'],
            author = comment_data['author'],
            post = comment_data['post']
            )

class UserModelTests(TestCase):
    def test_user_is_able_to_make_friends(self):
        test_user1 = dummy_user(1)
        test_user2 = dummy_user(2)
        test_user1.save()
        test_user2.save()
        test_user1.profile.friends.add(test_user2.profile)
        self.assertIn(test_user2.profile, test_user1.profile.friends.all())

    def test_user_is_able_to_like_posts(self):
        test_user = dummy_user(1)
        test_post = dummy_post()
        test_user.save()
        test_user.profile.liked_posts.add(test_post)
        self.assertIn(test_post, test_user.profile.liked_posts.all())

    def test_user_is_able_to_like_comments(self):
        test_user = dummy_user(1)
        test_comment = dummy_comment()
        test_user.save()
        test_user.profile.liked_comments.add(test_comment)
        self.assertIn(test_comment, test_user.profile.liked_comments.all())

    def test_client_is_able_to_view_all_users(self):
        test_user = dummy_user(1)
        test_user.save()
        client = Client()
        response = client.get('/main/users/')
        self.assertEquals(response.status_code, 200)

    def test_client_is_able_to_view_a_single_user(self):
        test_user = dummy_user(1)
        test_user.save()
        response = self.client.get('/main/users/1/')
        self.assertEquals(response.status_code, 200)

    def test_client_is_able_to_create_a_user(self):
        user_data = {
                'username': 'test_user',
                'password': 'test',
                'email': 'test@test.com',
                }
        response = self.client.post('/main/users/new/', data=user_data)
        self.assertEquals(response.status_code, 200)

    def test_user_new_returns_a_401_when_invalid(self):
        user_data = {
                'username': 'test_user',
                'password': 'test',
                'email': 'test',
                }
        response = self.client.post('/main/users/new/', data=user_data)
        self.assertEquals(response.status_code, 400)

    def test_client_is_able_to_edit_a_user(self):
        test_user = dummy_user(1)
        edit_data = {'username': 'test_user2'}
        response = self.client.put('/main/users/edit/%d/' % test_user.id, content_type='application/json', data=edit_data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content)['data']['username'], 'test_user2')

    def test_user_edit_returns_a_401_when_invalid(self):
        test_user = dummy_user(1)
        edit_data = {'email': 'test'}
        response = self.client.put('/main/users/edit/%d/' % test_user.id, content_type='application/json', data=edit_data)
        self.assertEquals(response.status_code, 400)

    def test_client_is_able_to_delete_a_user(self):
        test_user = dummy_user(1)
        response = self.client.delete('/main/users/delete/%d/' % test_user.id)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(User.objects.filter(id=test_user.id)), 0)

    def test_client_is_able_to_authenticate(self):
        test_user = dummy_user(1)
        user_data = {
                'username': 'test_user_1',
                'password':'test'
                }
        response = self.client.post('/main/login/', data=user_data)
        self.assertEquals(response.status_code, 200)

class PostModelTests(TestCase):
    pass

class CommentModelTests(TestCase):
    pass
