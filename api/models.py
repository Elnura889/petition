from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'petition')  # Ensure each user can vote only once per petition

    def __str__(self):
        return f"{self.user.username} voted for {self.petition.title}"
