import json

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View, TemplateView
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict


from ratings.models import WeeklyRating


class RatingsHomeView(TemplateView):
    template_name = 'ratings/home.html'

ratings_home = RatingsHomeView.as_view()


class RatingsAPIGet(View):

    # def date_handler(self, obj):
    #     return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    def get(self, request, *args, **kwargs):
        rating_stats = WeeklyRating.objects.all().values('date', 'count', 'average', 'median')
        for stat in rating_stats:
            stat['date'] = stat['date'].isoformat()
            stat['average'] = str(stat['average'])
            stat['median'] = str(stat['median'])
        rating_stats = list(rating_stats)
        return HttpResponse(json.dumps(rating_stats), content_type="application/json")
        #return JsonResponse(json.dumps(rating_stats, default=self.date_handler))
        #return JsonResponse(rating_stats, safe=False)


    # def post(self, request, *args, **kwargs):
    #     pass
    # TODO

ratings_api_get = RatingsAPIGet.as_view()

        # return render_to_response('user_profiles/login.html', variables,
        #                           context_instance=RequestContext(request))
        #return HttpResponse(json.dumps(response_data), content_type="application/json")

    # def get_context_data(self, **kwargs):  # Exec 1st
    #     # self.project_slug = self.kwargs.get('project_slug', '')
    #     # self.project_slug = self.project_slug.lower() if self.project_slug else ''  # To lower if not None
    #     # context = {}
    #     # context['project_slug'] = self.project_slug  # Get user login form, i.e. can use standard AuthenticationForm
    #     # context['form'] = UserLoginForm(self.request.POST or None, auto_id=False)  # do not include label
    #     # if context['project_slug']:
    #     #     context['next_url'] = reverse('project_details', args=[context['project_slug'], ]) or '/'
    #     # else:
    #     #     context['next_url'] = self.request.GET.get('next', '/')
    #     return context