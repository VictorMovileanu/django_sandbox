from django.test import TestCase

from testing.models import Profile


class FixtureTests(TestCase):
    fixtures = ['Profiles.json', 'Events.json']

    def test_fixtures(self):
        self.assertEquals(Profile.objects.count(), 200)
        pass
