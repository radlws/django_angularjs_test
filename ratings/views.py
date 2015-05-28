from django.views.generic import TemplateView


class RatingsHomeView(TemplateView):
    template_name = 'ratings/base.html'

ratings_home = RatingsHomeView.as_view()
