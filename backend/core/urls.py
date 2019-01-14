from django.urls import path
from core import views

urlpatterns=[
    path('',views.TestListView.as_view()),
    path('getpics/',views.PhotoListView.as_view()),
    path('reg/',views.RegView),
    path('<pk>',views.TestDetailView.as_view()),
]