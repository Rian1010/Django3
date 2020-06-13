from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestDjango(TestCase):

    def test_this_thing_works(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # Check if there is a name key in the dictionary of from errors
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test todo item'})
        self.assertTrue(form.is_valid)

    def test_form_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
