from django.views import generic
from django.db.models import Q
from .api import get_match_data, get_player_data
from .models import Player, Match


class IndexView(generic.TemplateView):
    get_player_data()
    get_match_data()
    template_name = 'lunaro/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all().order_by('-rank')[:3]
        context['matches'] = Match.objects.all().order_by('-time')[:3]
        return context


class PlayerView(generic.ListView):
    get_player_data()
    template_name = 'lunaro/players.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.all().order_by('-rank')


class MatchView(generic.ListView):
    get_match_data()
    template_name = 'lunaro/matches.html'
    context_object_name = 'matches'

    def get_queryset(self):
        return Match.objects.all().order_by('-time')


class MatchDetailView(generic.DetailView):
    model = Match
    template_name = 'lunaro/match_details.html'


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'lunaro/player_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_matches'] = Match.objects.filter(
            Q(player_a_id=self.kwargs['pk']) | Q(player_b_id=self.kwargs['pk']))
        return context
