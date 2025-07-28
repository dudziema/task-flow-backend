from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Task(models.Model):
  STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
  ]

  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
  deadline = models.DateTimeField(null=True, blank=True)
  project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} ({self.get_status_display()})"