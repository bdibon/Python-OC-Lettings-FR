from django.urls import path

import views


urlpatterns = [
    path('lettings/', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
