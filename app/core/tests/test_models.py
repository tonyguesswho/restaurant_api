from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='teast@gmail.com', password='password'):
    """Creare a sample user"""

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        """test creating user with email is successful"""
        email = 'test@gmail.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test that new user is normalized"""
        email = "test@GMAIL.com"
        user = get_user_model()\
            .objects.create_user(email=email, password='test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test invalid email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testp')

    def test_create_superuser(self):
        """Test create new super user is successful"""

        user = get_user_model().objects.create_superuser(
            'super@gmail.com', 'pass'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """create tag string representation"""

        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """create ingrdient string representation"""

        incredient = models.Ingredient\
            .objects.create(user=sample_user(), name='salt')
        self.assertEqual(str(incredient), incredient.name)

    def test_recipe_str(self):
        """Test recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Jollof rice',
            time_minutes=5,
            price=5.00)
        self.assertEqual(str(recipe), recipe.title)
