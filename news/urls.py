from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='main'),
    path('search/', Search.as_view(), name='search'),
    path('users/', UserView.as_view(), name='users'),
    path("users/<slug:slug>/", UserDetailView.as_view(), name='user_detail'),
    # path("users/<username>/change_profile", UserChange.as_view(), name='user_change'),
    # re_path('users/(?P<slug>[-a-zA-Z0-9_]+)/change_profile/', UserChange.as_view(),
    #         name='change_profile'),
    path("news/", NewsListView.as_view(), name='news'),
    # path("news/<slug:slug>/", NewsDetailView.as_view(), name='news_detail'),
    path("news/<slug>", NewsDetailView.as_view(), name='news_detail'),
    path('comments/<int:pk>/', AddComments.as_view(), name='add_comments'),
    path('teams/', TeamView.as_view(), name='teams'),
    path("team/<slug:slug>/", TeamDetailView.as_view(), name='team_detail'),
    path('teams/team_create/', CreateTeam.as_view(), name='team_create'),
    path('join/<int:pk>/', JoinTeam.as_view(), name='join_team'),
    path('teams/<int:pk>/exit/', TeamExit.as_view(), name='team_exit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('news_add/', AddNews.as_view(), name='news_add'),
    path('tournaments/', TournamentView.as_view(), name='tournaments'),
    path("tournaments/<slug:slug>/", TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournament_add/', AddTournament.as_view(), name='tournament_add'),
    path('tournament_registration/<int:pk>/', TournamentsRegistration.as_view(),
         name='tournament_registration'),
]