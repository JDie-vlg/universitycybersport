import random
import string
import time
from datetime import date

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from django.db.models import Q

from universitycybersport import REDIRECT_FIELD_NAME
from .models import *
from .forms import *


class HomeView(View):

    def get(self, request, *args, **kwargs):
        last_five_news = News.objects.order_by('-publish_date', '-publish_time')[:5]
        news = News.objects.all()
        tournaments = Tournaments.objects.all()
        context = {'last_five_news': last_five_news, 'news': news, 'tournaments': tournaments}
        return render(request, 'home.html', context)


class NewsListView(ListView):
    model = News
    queryset = News.objects.order_by('-publish_date', '-publish_time')


class NewsDetailView(DetailView):
    model = News
    slug_field = "slug"


class AddNews(News, View):

    def get(self, request, *args, **kwargs):
        form = AddNewsForm(request.POST or None)
        news = News.objects.all()
        context = {'form': form, 'news': news}
        return render(request, 'news/news_add.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        error = ''
        if request.method == 'POST':
            form = AddNewsForm(request.POST or None, request.FILES)
            form.author = request.user
            if form.is_valid():
                new = form.save(commit=False)
                new.author = request.user
                new.publish_time = date.today()
                new.publish_time = time.strftime('%H:%M')
                new.save()
                # form.save()
                return redirect('/news')
            else:
                error = form.errors
        form = AddNewsForm()
        context = {
            'form': form,
            'error': error,
        }
        return render(request, 'news/news_add.html', context)


class AddComments(LoginRequiredMixin, View):

    def post(self, request, pk):
        print(f'{request.POST} & {request.GET}')
        form = CommentsForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())


class TeamView(ListView):
    model = Team
    template_name = 'teams/teams_list.html'
    queryset = Team.objects.all()


class TeamDetailView(DetailView):
    model = Team
    template_name = 'teams/teams_detail.html'
    slug_field = "slug"


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return str(rand_string)


class CreateTeam(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        print(request.POST)
        profile = request.user.profile
        error_msg = 'У вас уже есть команда!'
        if request.method == 'POST':
            form = CreateTeamForm(request.POST, request.FILES)
            key_form = CreateKeyForm(request.POST)
            role = Role.objects.get(id=1)
            if form.is_valid():
                team = form.save()
                key = key_form.save(commit=False)
                key.team = team
                key.key = generate_alphanum_random_string(20)
                key.save()
                profile.team = team
                profile.role = role
                profile.save()
                return redirect('teams')
        form = CreateTeamForm()
        context = {'form': form,
                   'error_msg': error_msg}
        return render(request, 'teams/team_create.html', context)


class JoinTeam(LoginRequiredMixin, View):

    def get(self, request, pk):
        print(f'post:{request.POST}, get:{request.GET}')
        form = JoinTeamForm(request.POST or None)
        team = Team.objects.get(id=pk)
        context = {'form': form,
                   'team': team
                   }
        return render(request, 'teams/teams_detail.html', context)

    def post(self, request, pk):
        if request.method == 'POST':
            form = JoinTeamForm(request.POST)
            team = Team.objects.get(id=pk)
            error_msg = 'Неверный код'
            if form.is_valid() and request.user.is_authenticated:
                # valid_key = Key.objects.all()
                key = form.cleaned_data['key']  # get key from form
                db_key = Key.objects.filter(key=key).first()  # get key from db
                role = Role.objects.get(id=2)
                # db_key is not None and
                if str(db_key) == str(key) and team.id == db_key.team.id:
                    request.user.profile.team = team
                    request.user.profile.role = role
                    request.user.profile.save()
                    # profile = Profile(
                    #     role_id=role.id,
                    #     team_id=db_key.team.id,
                    #     user_id=request.user.id,
                    #     nickname=request.user.profile.nickname,
                    # )
                    # profile.save()
                else:
                    return HttpResponse(error_msg)
            return redirect(team.get_absolute_url())


class TeamExit(View):

    def post(self, request, pk):
        if request.method == 'POST':
            form = ExitTeamForm(request.POST or None)
            team = Team.objects.get(id=pk)
            if form.is_valid():
                request.user.profile.team = None
                request.user.profile.role = None
                request.user.profile.save()
                return redirect(team.get_absolute_url())




class TournamentView(ListView):
    model = Tournaments
    template_name = 'tournaments/tournaments_list.html'
    queryset = Tournaments.objects.all()


class TournamentDetailView(DetailView):
    model = Tournaments
    template_name = 'tournaments/tournaments_detail.html'
    slug_field = "slug"


class AddTournament(Tournaments, View):

    def get(self, request, *args, **kwargs):
        form = AddTournamentForm(request.POST or None)
        tournament = Tournaments.objects.all()
        context = {'form': form, 'tournament': tournament}
        return render(request, 'tournaments/tournaments_add.html', context)

    def post(self, request, *args, **kwargs):
        error = ''
        if request.method == 'POST':
            form = AddTournamentForm(request.POST or None, request.FILES)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.save()
                return redirect('/tournaments/')
            else:
                error = 'ERROR'
        form = AddTournamentForm()
        context = {
            'form': form,
            'error': error,
        }
        return render(request, 'tournaments/tournaments_add.html', context)


class TournamentsRegistration(LoginRequiredMixin, View):

    def post(self, request, pk):
        print(f'{request.POST} & {request.GET}')
        form = TournamentsRegistrationForm(request.POST)
        tournaments = Tournaments.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.tournaments = tournaments
            form.save()
        return redirect(tournaments.get_absolute_url())


class UserView(ListView):
    model = User
    template_name = 'user/profile_list.html'
    queryset = User.objects.all()

    def username_view(self, request):
        user = User.objects.get(username=request.POST['username'])
        last_login = user.last_login
        return last_login


class UserDetailView(DetailView):
    model = Profile
    template_name = 'user/profile_detail.html'
    slug_field = 'nickname'


class LoginView(Profile, View):
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_authenticated_user = False
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return redirect_to
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get(self, request, *args, **kwargs):
        print(f'ТУТ СМОТРИ {self.get_success_url()}')
        form = LoginForm(request.POST or None)
        author = Profile.objects.all()
        context = {'form': form, 'author': author}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        print(f'ТУТ СМОТРИ {request.path_info} {request.build_absolute_uri()} {request.get_full_path()}')
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(self.get_success_url())
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)


class RegistrationView(View):
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}

    def get_next_page(self):
        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        else:
            next_page = self.next_page

        if (self.redirect_field_name in self.request.POST or
                self.redirect_field_name in self.request.GET):
            next_page = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get(self, request, *args, **kwargs):
        print(f'ТУТ СМОТРИ {self.get_next_page()}')
        form = RegistrationForm(request.POST or None)
        author = Profile.objects.all()
        context = {'form': form, 'author': author}
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.nickname = form.cleaned_data['nickname']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(
                user=new_user,
                nickname=new_user,
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(self.get_next_page())
        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)


class Search(ListView):

    def get_queryset(self):
        return News.objects.filter(Q(title__icontains=self.request.GET.get('string')) |
                                   Q(author__profile__nickname__icontains=self.request.GET.get('string'))
                                   )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['string'] = self.request.GET.get('string')
        return context
