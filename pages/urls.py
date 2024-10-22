from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomePageView,
    TADetailView, 
    TACreateView,
    TAUpdateView,
    TADeleteView,
    TAListView,

)

urlpatterns = [

    path("post/new/", TACreateView.as_view(), name="ta_new"),
    path("post/<int:pk>/", TADetailView.as_view(), name="ta_detail"),
    path("post/<int:pk>/edit/", TAUpdateView.as_view(), name="ta_edit"),
    path("post/<int:pk>/delete/", TADeleteView.as_view(), name="ta_delete"),
    path("", TAListView.as_view(), name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
