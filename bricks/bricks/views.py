import json
import datetime as dt
from collections import defaultdict
from itertools import groupby

from django.http import (
    HttpResponse, HttpResponseNotFound,
    HttpResponseBadRequest, JsonResponse)
from django.shortcuts import get_object_or_404

from .models import Building, History


def building(request):
    if request.method != 'POST':
        return HttpResponseNotFound()
    data = json.loads(request.body)
    if 'address' not in data or 'year' not in data:
        return HttpResponseBadRequest()

    building_obj = Building(**data)
    building_obj.save()
    return JsonResponse({
        'id': building_obj.building_id,
        'address': building_obj.address,
        'year': building_obj.year
        }, status=201)


def bricks(request, building_id):
    if request.method != 'POST':
        return HttpResponseNotFound()
    data = json.loads(request.body)
    if 'num' not in data or 'date' not in data:
        return HttpResponseBadRequest()
    try:
        date = dt.datetime.strptime(data['date'], '%Y-%m-%d').date()
    except ValueError:
        return HttpResponseBadRequest()

    building_obj = get_object_or_404(Building, building_id=building_id)
    history_obj = History(
        building=building_obj,
        bricks_num=data['num'],
        date=date)
    history_obj.save()
    return HttpResponse(status=201)


def stats(request):
    if request.method != 'GET':
        return HttpResponseNotFound()

    history = History.objects.all()
    history = sorted(history, key=lambda x: x.date)
    buildings = Building.objects.all()

    current = defaultdict(int)
    result = defaultdict(lambda: defaultdict(dict))
    for date, date_history in groupby(history, key=lambda x: x.date):
        # iterate bricks arrived on this date
        for h_elem in date_history:
            id_ = h_elem.building.building_id
            current[id_] += h_elem.bricks_num
        # write stats by building
        for building in buildings:
            id_ = building.building_id
            result[str(date)][id_] = {
                'address': building.address,
                'year': building.year,
                'bricks': current[id_]
            }

    result = {k: dict(v) for k, v in result.items()}
    return JsonResponse(result)
