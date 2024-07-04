from django.test import TestCase
from tabom.models import User, Article
from tabom.service import do_like


class TestLikeService(TestCase):

    def test_a_user_can_like_an_article(self) -> None:
        # Given test 대상이 되는 재료 생성
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test article")

        # When test의 메인 행동
        like = do_like(user.id, article.id)

        # Then 결과 확인
        self.assertIsNotNone(like)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)


    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_article")

        # Expect
        like1 = do_like(user.id, article.id)
        with self.assertRaises(Exception):
            like2 = do_like(user.id, article.id)



