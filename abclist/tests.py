from django.test import TestCase
from abclist.models import ABCList

class ABCListTestCase(TestCase):
    def setUp(self):
        ABCList.objects.create(user='twe', abclist={'a':"Alpha", 'b': "Beta"})
        ABCList.objects.create(user='twe', abclist={'c': "Ceta", 'd': "Delta"})

    def test_abclist_encoding(self):
        """The abclist is encoded correcty as JSON dump"""
        abcs = ABCList.objects.all()[:1].get()

        expected_dict = {'a': 'Alpha', 'b': 'Beta'}
        self.assertEqual(abcs.abclist, expected_dict)

