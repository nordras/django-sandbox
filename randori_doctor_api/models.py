from django.db import models

class Room(models.Model):
    class RoomStatus(models.TextChoices):
        ACTIVE = 'active', 'Active'
        FINISHED = 'finished', 'Finished'

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=RoomStatus.choices, default=RoomStatus.ACTIVE)

    def __str__(self):
        return self.name

class Leader(models.Model):
    name = models.CharField(max_length=100)
    slack_handle = models.CharField(max_length=100)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='leader')
    zoom_link = models.URLField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    class Role(models.TextChoices):
        PILOT = 'pilot', 'Pilot'
        COPILOT = 'copilot', 'Copilot'
        OBSERVER = 'observer', 'Observer'

    name = models.CharField(max_length=100)
    slack_handle = models.CharField(max_length=100)
    current_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='participants')
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.OBSERVER)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Session(models.Model):
    current_round = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_running = models.BooleanField(default=False)

    def __str__(self):
        return f"Session {self.pk} (Round {self.current_round})"
