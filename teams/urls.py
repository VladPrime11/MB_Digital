from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.person_views import PersonViewSet
from teams.team_views import TeamViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
