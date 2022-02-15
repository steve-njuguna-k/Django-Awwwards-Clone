from django.contrib.auth.models import User
from django.test import TestCase
from .models import Portfolio, Profile, Rating

class TestUserProfile(TestCase):
    def setUp(self):
        self.new_user=User(first_name='John', last_name='Doe', username='user', email='user@gmail.com',password='user')
        self.new_user.save()

        self.profile=Profile(
            author=self.new_user, 
            bio='this is me', 
            profile_image='profile.jpg',
            country = 'Kenya',
            personal_website = 'personalsite.com',
            github_link = 'github.com',
            instagram_link = 'instagram.com',
            linkedin_link = 'linkedin.com',
            twitter_link = 'twitter.com',
            email_confirmed = True
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class PortfolioTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com"
        )

        self.portfolio = Portfolio(
            portfolio_image = "default.jpg",
            title="Portfolio 1",
            caption="Test Caption",
            portfolio_site_url="url.com",
            repo_url="github.com",
            primary_language="django",
            category="Professional",
            author=user,
            profile = user.profile
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.portfolio, Portfolio))

    def test_save_method(self):
        self.portfolio.save_Portfolio()
        Portfolios = Portfolio.objects.all()
        self.assertTrue(len(Portfolios) > 0)
    
    def test_update_portfolio(self):
        self.portfolio.save_Portfolio()
        Portfolios = Portfolio.objects.all()
        self.assertTrue(len(Portfolios) > 0)

    def test_delete_method(self):
        self.portfolio.save_Portfolio()
        self.portfolio.delete_Portfolio()
        Portfolios = Portfolio.objects.all()
        self.assertTrue(len(Portfolios) == 0)

class RatingTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com"
        )

        self.portfolio = Portfolio(
            portfolio_image = "default.jpg",
            title="Portfolio 1",
            caption="Test Caption",
            portfolio_site_url="url.com",
            repo_url="github.com",
            primary_language="django",
            category="Professional",
            author=user,
            profile = user.profile
        )

        self.rating = Rating(
            comment = 'New Comment',
            design_rating = 6,
            usability_rating = 8,
            content_rating = 7,
            creativity_rating = 8,
            experience_rating = 6,
            avarage_rating = 7,
            author=user,
            profile = user.profile
            portfolio = self.portfolio
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))