from typing import Any, Dict
from django.views.generic import ListView
from ..models.article import Article


class HomePageView(ListView):
    model = Article
    template_name = 'forum.html'
    queryset = Article.objects.all().order_by('-created')[:10]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
