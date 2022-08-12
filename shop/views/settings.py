from django.views.generic import FormView

from shop.models.article import Article
from ..forms.settings import SettForm
from typing import Any, Dict
from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import redirect
from django.urls import reverse_lazy

class SettingsView(FormView):
    form_class = SettForm
    template_name = "settings.html"
    success_url = reverse_lazy('settings')

    def form_valid(self, form: SettForm):
        # title = form.cleaned_data['title']
        # synopsis = form.cleaned_data['synopsis']
        # img = form.cleaned_data['img']
        # url = form.cleaned_data['url']
        # try:
        #     Article.objects.create(
        #         title=title,
        #         synopsis=synopsis,
        #         img=img,
        #         url=url
        #     )
        try:
            form.save()
        except DatabaseError as e:
            messages.success(
                self.request, "Unsuccessful publish. DatabaseError")
            return redirect('settings')
        messages.success(self.request, "Successful publish.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful publish. Invalid information.")
        return super().form_invalid(form)