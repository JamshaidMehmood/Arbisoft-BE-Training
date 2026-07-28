from django.test import TestCase
from django.urls import reverse

from core.items import ITEMS


class HelloViewTests(TestCase):
    def test_greets_the_name_from_the_url(self):
        response = self.client.get(reverse('core:hello', args=['Jamshaid']))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain; charset=utf-8')
        self.assertEqual(response.content.decode(), 'Hello, Jamshaid! Welcome to Django.\n')

    def test_rejects_non_get_methods(self):
        response = self.client.post(reverse('core:hello', args=['Jamshaid']))

        self.assertEqual(response.status_code, 405)


class ItemListViewTests(TestCase):
    def test_lists_every_item(self):
        response = self.client.get(reverse('core:item-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/item_list.html')
        self.assertEqual(len(response.context['items']), len(ITEMS))

    def test_items_are_ordered_by_id(self):
        response = self.client.get(reverse('core:item-list'))

        ids = [item['id'] for item in response.context['items']]
        self.assertEqual(ids, sorted(ids))


class ItemDetailViewTests(TestCase):
    def test_shows_the_requested_item(self):
        response = self.client.get(reverse('core:item-detail', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/item_detail.html')
        self.assertEqual(response.context['item']['id'], 1)
        self.assertContains(response, 'Keyboard')

    def test_returns_404_for_an_unknown_id(self):
        response = self.client.get(reverse('core:item-detail', args=[999]))

        self.assertEqual(response.status_code, 404)
