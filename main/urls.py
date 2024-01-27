from django.urls import path
from .views import get_user_view, gp_user_view, TeacherList

urlpatterns = [
    path('get-user/', get_user_view, name='user'),
    path('gp-user/', gp_user_view, name='gp-user'),
    path('teachers/', TeacherList.as_view(), name='teachers'),
]