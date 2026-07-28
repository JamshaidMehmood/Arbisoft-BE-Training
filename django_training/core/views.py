from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, ListView

from core.items import all_items, get_item


@require_GET
def hello(request, name):
    """Greet `name` with a plain-text response."""
    return HttpResponse(
        f'Hello, {name}! Welcome to Django.\n',
        content_type='text/plain; charset=utf-8',
    )


class ItemListView(ListView):
    """List every item.

    `ListView` only needs an iterable, so a plain list works in place of a
    QuerySet until there is a model to query.
    """

    template_name = 'core/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return all_items()


class ItemDetailView(DetailView):
    """Show a single item, looked up by the `id` captured from the URL."""

    template_name = 'core/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        return get_item(self.kwargs[self.pk_url_kwarg])
