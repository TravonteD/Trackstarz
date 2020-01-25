from django.test import TestCase

from .models import *

def dummy_user():
    user_data = {
            'username': 'test_user',
            'displayname': 'test_user',
            'email': 'test@test.com',
            }
    return User.objects.create(
            username = user_data['username'],
            displayname = user_data['displayname'],
            email = user_data['email']
            )

def dummy_post():
    post_data = {
            'title': 'test title',
            'content': 'test content',
            'author': dummy_user()
            }
    return Post.objects.create(
            title = post_data['title'],
            content = post_data['content'],
            author = post_data['author']
            )

def dummy_comment():
    comment_data = {
            'content': 'test content',
            'author': dummy_user(),
            'post': dummy_post()
            }
    return Comment.objects.create(
            content = comment_data['content'],
            author = comment_data['author'],
            post = comment_data['post']
            )

class UserModelTests(TestCase):
    def test_user_is_able_to_make_friends(self):
        test_user1 = dummy_user()
        test_user2 = dummy_user()
        test_user1.save()
        test_user2.save()
        test_user1.friends.add(test_user2)
        self.assertIn(test_user2, test_user1.friends.all())

    def test_user_is_able_to_like_posts(self):
        test_user = dummy_user()
        test_post = dummy_post()
        test_user.save()
        test_user.liked_posts.add(test_post)
        self.assertIn(test_post, test_user.liked_posts.all())

    def test_user_is_able_to_like_comments(self):
        test_user = dummy_user()
        test_comment = dummy_comment()
        test_user.save()
        test_user.liked_comments.add(test_comment)
        self.assertIn(test_comment, test_user.liked_comments.all())

class PostModelTests(TestCase):
    pass

class CommentModelTests(TestCase):
    pass
