from django.db import models

# Create your models here.
#CREATE TABLE login(username VARCHAR(50))

class Login(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField( )

class Club (models.Model):
    club_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=20)
    stadium = models.CharField(max_length=30)
    capacity = models.IntegerField()
    manager = models.CharField(max_length=30)
    def __str__(self):
        return self.club_name


class Player(models.Model):
    club = models.ForeignKey(Club,on_delete = models.CASCADE,null=True,blank=True)
    GENDER_OPTIONS =[
        ("M","MALE"),
        ("F","FEMALE")
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    position = models.CharField(max_length=30)
    shirt_number = models.IntegerField()
    birth_year = models.DateField()

class Season(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

class Fixture(models.Model):
    home_club = models.CharField(max_length=30)
    away_club = models.CharField(max_length=30)
    stadium = models.CharField(max_length=30)
    Match_time = models.TimeField()
    match_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)

    season = models.ForeignKey(
    Season,
    on_delete=models.PROTECT,
    related_name='fixtures',
    null=True,
    blank=True
)

    home_club_relation = models.ForeignKey(
    Club,
    on_delete=models.PROTECT,
    related_name='home_fixtures',
    null=True,
    blank=True
)
    away_club_relation = models.ForeignKey(
    Club,
    on_delete=models.PROTECT,
    related_name='away_fixtures',
    null=True,
    blank=True
)
    def __str__(self):
        return f"{self.home_club} vs {self.away_club}"


class Results(models.Model):
    fixture = models.OneToOneField(
        Fixture,
        on_delete=models.CASCADE,
        null= True,
        blank=True
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.PROTECT,
        related_name='results',
        null=True,
        blank=True
    )
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()

    def __str__(self):
        return f"{self.fixture}"
    


  
class Statistics(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        related_name='statistics',
        null=True,
        blank=True
    )

    season = models.ForeignKey(
        Season,
        on_delete=models.PROTECT,
        related_name='statistics',
        null=True,
        blank=True
    )

    result = models.ForeignKey(
        Results,
        on_delete=models.PROTECT,
        related_name='statistics',
        null=True,
        blank=True
    )

    points = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    possession = models.CharField(max_length=20)


    