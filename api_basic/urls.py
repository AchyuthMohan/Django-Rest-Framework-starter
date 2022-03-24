from django.urls import path
from api_basic import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
urlpatterns=format_suffix_patterns(urlpatterns)