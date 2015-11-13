from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^all/$', views.RestaurantViewList.as_view()),
    url(r'^rule/$', views.GetRestaurant.as_view()),
]
