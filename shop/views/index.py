from audioop import reverse
from typing import Any, Dict
from django.views.generic import ListView
from ..models.article import Article


class HomePageView(ListView):
    model = Article
    template_name = "forum.html"
    queryset = Article.objects.filter().order_by('-created')[:3]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
