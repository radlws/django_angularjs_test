from django.views.generic import TemplateView


class TestVerbatimView(TemplateView):

    template_name = 'test_verbatim.html'

    #def get(self, request, *args, **kwargs):


test_verbatim = TestVerbatimView.as_view()


class TestInterpolationView(TemplateView):

    template_name = 'test_interpolation.html'

    #def get(self, request, *args, **kwargs):


test_interpolation = TestInterpolationView.as_view()