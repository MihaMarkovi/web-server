from django.db import models


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    player_a = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_a")
    player_b = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_b")
    score_a = models.SmallIntegerField()
    score_b = models.SmallIntegerField()
    ping_a = models.SmallIntegerField()
    ping_b = models.SmallIntegerField()
    delta_a = models.SmallIntegerField()
    delta_b = models.SmallIntegerField()
    time = models.DateTimeField('time')

    def __str__(self):
        return self.player_a.name + " vs " + self.player_b.name
