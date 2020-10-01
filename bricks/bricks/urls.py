from django.urls import path

import bricks.views as views

urlpatterns = [
    path('building/', views.building),
    path('building/<int:building_id>/add-bricks/', views.bricks),
    path('stats/', views.stats),
]
