from django.urls import path
from . import views

# Lunaro urls


urlpatterns = [
    path('', views.IndexView.as_view(), name="lunaro-index"),
    path('/players', views.PlayerView.as_view(), name="leaderboard"),
    path('/matches', views.MatchView.as_view(), name="matches"),
    path('/matches/<int:pk>', views.MatchDetailView.as_view(), name="match-details")
]
