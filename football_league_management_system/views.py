from django.shortcuts import render


from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Club,Player,Season,Fixture,Results,Statistics
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login2.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login2.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_page(request):
    return render(request, 'home2.html')

@login_required(login_url='login')
def club_page(request):
    if request.method == 'POST':
        club_name = request.POST.get('club_name')
        nick_name = request.POST.get('nick_name')
        stadium = request.POST.get('stadium')
        capacity = request.POST.get('capacity')
        manager = request.POST.get('manager')

        Club.objects.create(
            club_name=club_name,
            nick_name=nick_name,
            stadium=stadium,
            capacity=capacity,
            manager=manager
        )
    clubs = Club.objects.all()
    return render(request, 'club2.html',{'clubs': clubs})

@login_required(login_url='login')
def edit_club(request, club_id):
    club = Club.objects.get(id=club_id)

    if request.method == 'POST':
        club.club_name = request.POST.get('club_name')
        club.nick_name = request.POST.get('nick_name')
        club.stadium = request.POST.get('stadium')
        club.capacity = request.POST.get('capacity')
        club.manager = request.POST.get('manager')

        club.save()
        return redirect('club')

    return render(request, 'edit_club.html', {'club': club})

@login_required(login_url='login')
def delete_club(request, club_id):
    club = Club.objects.get(id=club_id)

    if request.method == 'POST':
        club.delete()
        return redirect('club')

    return render(request, 'delete_club.html', {'club': club})


@login_required(login_url='login')
def player_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        shirt_number = request.POST.get('shirt_number')
        birth_year = request.POST.get('birth_year')

        Player.objects.create(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            position=position,
            shirt_number=shirt_number,
            birth_year=birth_year
        )
        return redirect('player')
    players = Player.objects.all()

    return render(request, 'player2.html', {'players': players})

@login_required(login_url='login')
def edit_player(request, player_id):

    player = Player.objects.get(id=player_id)

    if request.method == 'POST':
        player.first_name = request.POST.get('first_name')
        player.last_name = request.POST.get('last_name')
        player.gender = request.POST.get('gender')
        player.position = request.POST.get('position')
        player.shirt_number = request.POST.get('shirt_number')
        player.birth_year = request.POST.get('birth_year')

        player.save()
        return redirect('player')

    return render(request, 'edit_player.html', {'player': player})

@login_required(login_url='login')
def delete_player(request, player_id):
    player = Player.objects.get(id=player_id)

    if request.method == 'POST':
        player.delete()
        return redirect('player')

    return render(request, 'delete_player.html', {'player': player})

@login_required(login_url='login')
def season_page(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(request.POST)
        print("START DATE:", start_date)
        print("END DATE:", end_date)

        Season.objects.create(
            start_date=start_date,
            end_date=end_date
        )

        return redirect('season')

    seasons = Season.objects.all()

    return render(request, 'season2.html', {
        'seasons': seasons,
        'today': timezone.now().date()
    })

@login_required(login_url='login')
def edit_season(request, season_id):
    season = Season.objects.get(id=season_id)

    if request.method == 'POST':
        season.start_date = request.POST.get('start_date')
        season.end_date = request.POST.get('end_date')

        season.save()

        return redirect('season')

    return render(request, 'edit_season.html', {
        'season': season
    })

@login_required(login_url='login')
def delete_season(request, season_id):
    season = Season.objects.get(id=season_id)

    if request.method == 'POST':
        season.delete()
        return redirect('season')

    return render(request, 'delete_season.html', {
        'season': season
    })


@login_required(login_url='login')
def matchfixture_page(request):

    if request.method == 'POST':
        home_club = request.POST.get('home_club')
        away_club = request.POST.get('away_club')
        stadium = request.POST.get('stadium')
        Match_time = request.POST.get('Match_time')
        match_date = request.POST.get('match_date') or None
        status = request.POST.get('status')

        Fixture.objects.create(
            home_club=home_club,
            away_club=away_club,
            stadium=stadium,
            Match_time=Match_time,
            match_date=match_date,
            status=status
        )

        return redirect('matchfixture')

    fixtures = Fixture.objects.all()

    return render(request, 'matchfixture2.html', {
        'fixtures': fixtures
    })

@login_required(login_url='login')
def edit_fixture(request, fixture_id):

    fixture = Fixture.objects.get(id=fixture_id)

    if request.method == 'POST':
        fixture.home_club = request.POST.get('home_club')
        fixture.away_club = request.POST.get('away_club')
        fixture.stadium = request.POST.get('stadium')
        fixture.Match_time = request.POST.get('Match_time')
        fixture.match_date = request.POST.get('match_date') or None
        fixture.status = request.POST.get('status')

        fixture.save()

        return redirect('matchfixture')

    return render(request, 'edit_fixture.html', {
        'fixture': fixture
    })

@login_required(login_url='login')
def delete_fixture(request, fixture_id):

    fixture = Fixture.objects.get(id=fixture_id)

    if request.method == 'POST':
        fixture.delete()
        return redirect('matchfixture')

    return render(request, 'delete_fixture.html', {
        'fixture': fixture
    })


@login_required(login_url='login')
def results_page(request):

    if request.method == 'POST':
        fixture_id = request.POST.get('fixture')
        season_id = request.POST.get('season')
        goals_scored = request.POST.get('goals_scored')
        goals_conceded = request.POST.get('goals_conceded')
        Results.objects.create(
            fixture_id=fixture_id,
            season_id=season_id,
            goals_scored=goals_scored,
            goals_conceded=goals_conceded
        )

        return redirect('results')
    results = Results.objects.all()

    fixtures = Fixture.objects.all()
    seasons = Season.objects.all()

    return render(request, 'results2.html', {
        'results': results,
        'fixtures': fixtures,
        'seasons': seasons
    })

@login_required(login_url='login')
def edit_results(request, result_id):
    result = Results.objects.get(id=result_id)

    if request.method == 'POST':
        result.fixture_id = request.POST.get('fixture')
        result.season_id = request.POST.get('season')
        result.goals_scored = request.POST.get('goals_scored')
        result.goals_conceded = request.POST.get('goals_conceded')

        result.save()

        return redirect('results')

    fixtures = Fixture.objects.all()
    seasons = Season.objects.all()

    return render(request, 'edit_results.html', {
        'result': result,
        'fixtures': fixtures,
        'seasons': seasons
    })

@login_required(login_url='login')
def delete_result(request, result_id):
    result = Results.objects.get(id=result_id)

    if request.method == 'POST':
        result.delete()
        return redirect('results')

    return render(request, 'delete_result.html', {
        'result': result
    })

@login_required(login_url='login')
def statistics_page(request):

    if request.method == 'POST':
        club_id = request.POST.get('club')
        season_id = request.POST.get('season')
        result_id = request.POST.get('result')
        points = request.POST.get('points')
        yellow_cards = request.POST.get('yellow_cards')
        red_cards = request.POST.get('red_cards')
        possession = request.POST.get('possession')

        Statistics.objects.create(
            club_id=club_id,
            season_id=season_id,
            result_id=result_id,
            points=points,
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            possession=possession
        )

        return redirect('statistics')

    statistics = Statistics.objects.all()
    clubs = Club.objects.all()
    seasons = Season.objects.all()
    results = Results.objects.all()

    return render(request, 'statistics2.html', {
        'statistics': statistics,
        'clubs': clubs,
        'seasons': seasons,
        'results': results
    })

@login_required(login_url='login')
def edit_statistics(request, statistics_id):

    statistic = Statistics.objects.get(id=statistics_id)

    if request.method == 'POST':
        statistic.club_id = request.POST.get('club')
        statistic.season_id = request.POST.get('season')
        statistic.result_id = request.POST.get('result')
        statistic.points = request.POST.get('points')
        statistic.yellow_cards = request.POST.get('yellow_cards')
        statistic.red_cards = request.POST.get('red_cards')
        statistic.possession = request.POST.get('possession')

        statistic.save()

        return redirect('statistics')

    clubs = Club.objects.all()
    seasons = Season.objects.all()
    results = Results.objects.all()

    return render(request, 'edit_statistics.html', {
        'statistic': statistic,
        'clubs': clubs,
        'seasons': seasons,
        'results': results
    })

@login_required(login_url='login')
def delete_statistics(request, statistics_id):

    statistic = Statistics.objects.get(id=statistics_id)

    if request.method == 'POST':
        statistic.delete()
        return redirect('statistics')

    return render(request, 'delete_statistics.html', {
        'statistic': statistic
    })

