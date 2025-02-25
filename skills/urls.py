from django.urls import path
from .views import skills_detail, skills_list

urlpatterns = [
    path('',skills_list,name='skills-list'),
    path('<int:skill_id>/',skills_detail,name='skills-detail')
]