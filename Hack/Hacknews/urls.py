from .import views
from django.urls import path


urlpatterns = [
    path('', views.mymodelView.as_view(), name='mymodelView'),
    path('detail/<int:pk>/', views.mymodelViewDetail.as_view(), name='detail'),
    path('filter_job/', views.filter_job, name="filter_job"),
    path("display_all_items/", views.display_all_items, name='display_all_items'),
    path("detail_record/<int:id>/", views.detailView, name="detail_record"),
    path("search/", views.search_result, name='search')
]