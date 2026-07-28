"""In-memory item "repository".

Stands in for a database while the project has no models. Keeping the data and
its lookup helpers here means the views stay thin and swapping in a real
QuerySet later only touches this module.
"""

from django.http import Http404

ITEMS = (
    {
        'id': 1,
        'name': 'Keyboard',
        'category': 'Peripherals',
        'price': '49.99',
        'description': 'A mechanical keyboard with tactile switches.',
    },
    {
        'id': 2,
        'name': 'Monitor',
        'category': 'Displays',
        'price': '199.00',
        'description': 'A 27-inch 1440p display.',
    },
    {
        'id': 3,
        'name': 'Mouse',
        'category': 'Peripherals',
        'price': '29.50',
        'description': 'A wireless mouse with a silent scroll wheel.',
    },
    {
        'id': 4,
        'name': 'Desk Lamp',
        'category': 'Accessories',
        'price': '15.00',
        'description': 'An adjustable LED lamp with three brightness levels.',
    },
)


def all_items():
    """Return every item, ordered by id."""
    return sorted(ITEMS, key=lambda item: item['id'])


def get_item(item_id):
    """Return the item with `item_id`, or raise Http404 if there is none."""
    for item in ITEMS:
        if item['id'] == item_id:
            return item
    raise Http404(f'No item with id {item_id}.')
