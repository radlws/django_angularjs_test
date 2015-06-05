import json
import datetime

from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponse


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

    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        try:
            data = json.loads(request.body)
            WeeklyRating.objects.create(average=data.get('average'), date=now, median=data['median'], count=data['count'])
        except Exception as e:
            s = 200
            msg = {"status": "fail", "message": str(e)}
        else:
            s = 201
            msg = {"status": "success", "message": None}
        return JsonResponse(msg, status=s)

ratings_api = RatingsAPI.as_view()
