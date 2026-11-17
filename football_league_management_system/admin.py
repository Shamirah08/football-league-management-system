from django.contrib import admin

# Register your models here.

from.models import Login,Club,Player,Season,Fixture,Results,Statistics
from django.contrib import admin
from .models import Login, Club, Player, Season, Fixture, Results, Statistics


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'club_name',
        'nick_name',
        'stadium',
        'capacity',
        'manager'
    )

    search_fields = ('club_name', 'nick_name')

    list_filter = ('stadium',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display =(
        'first_name',
        'last_name',
        'club',
        'gender',
        'position',
        'shirt_number',
        'birth_year'
    )
    search_fields = ('first_name','last_name') 
    list_filter =('gender','club')
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display= (
        'start_date',
        'end_date',
    )  
    list_filter = ('start_date','end_date')
    ordering= ('start_date',)

@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'home_club',
        'away_club',
        'stadium',
        'Match_time',
        'status',
    )

    search_fields = ('home_club', 'away_club', 'stadium')

    list_filter = ('status', 'stadium')

    ordering = ('Match_time',)

@admin.register(Results)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'fixture',
        'season',
        'goals_scored',
        'goals_conceded',
    )
    search_fields = (
        'fixture__home_club',
        'fixture__away_club',)

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):

    list_display = (
        'club',
        'season',
        'points',
        'yellow_cards',
        'red_cards',
        'possession',

    )
    list_filter = ('points','yellow_cards','red_cards',)
    ordering = ('points',)

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')
    search_fields = ('username',)



