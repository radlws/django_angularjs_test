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


class RatingsAPI(View):

    def get(self, request, *args, **kwargs):
        rating_stats = WeeklyRating.objects.all().values('date', 'count', 'average', 'median')
        for stat in rating_stats:
            stat['date'] = stat['date'].isoformat()
            stat['average'] = str(stat['average'])
            stat['median'] = str(stat['median'])
        rating_stats = list(rating_stats)
        return HttpResponse(json.dumps(rating_stats), content_type="application/json")
        #return JsonResponse(rating_stats, safe=False)


    def post(self, request, *args, **kwargs):
        print 'i have been posted'
        msg = {"status": "success", "message": None}
        return JsonResponse(msg, status=201)

ratings_api = RatingsAPI.as_view()
