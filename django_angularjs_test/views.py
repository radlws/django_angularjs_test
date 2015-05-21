from django.views.generic import TemplateView


class TestVerbatimView(TemplateView):

    template_name = 'test_verbatim.html'

    #def get(self, request, *args, **kwargs):

test_verbatim = TestVerbatimView.as_view()


class TestInterpolationView(TemplateView):
    template_name = 'test_interpolation.html'
test_interpolation = TestInterpolationView.as_view()


class TestControllerView(TemplateView):
    template_name = 'test_controller.html'
test_controller = TestControllerView.as_view()