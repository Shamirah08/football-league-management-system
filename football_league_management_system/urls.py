from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    
    path('home/', views.home_page, name='home'),

    path('club/', views.club_page, name='club'),
    path('edit-club/<int:club_id>/', views.edit_club, name='edit_club'),
    path('delete-club/<int:club_id>/', views.delete_club, name='delete_club'),

    path('player/', views.player_page, name='player'),
    path('edit-player/<int:player_id>/', views.edit_player, name='edit_player'),
    path('delete-player/<int:player_id>/', views.delete_player, name='delete_player'),

    path('season/', views.season_page, name='season'),
    path('edit-season/<int:season_id>/', views.edit_season, name='edit_season'),
    path('delete-season/<int:season_id>/', views.delete_season, name='delete_season'),

    path('matchfixture/', views.matchfixture_page, name='matchfixture'),
    path('edit-fixture/<int:fixture_id>/', views.edit_fixture, name='edit_fixture'),
    path('delete-fixture/<int:fixture_id>/', views.delete_fixture, name='delete_fixture'),

    path('results/', views.results_page, name='results'),
    path('edit-results/<int:result_id>/', views.edit_results, name='edit_result'),
    path('delete-results/<int:result_id>/', views.delete_result, name='delete_result'),
    
    path('statistics/', views.statistics_page, name='statistics'),
    path('edit-statistics/<int:statistics_id>/', views.edit_statistics, name='edit_statistics'),
    path('delete-statistics/<int:statistics_id>/', views.delete_statistics, name='delete_statistics'),

]