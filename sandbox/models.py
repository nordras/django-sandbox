from django.db import models

# Models for the sandbox app (for experiments and learning)

class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
