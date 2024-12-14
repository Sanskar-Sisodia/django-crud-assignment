from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensures 'name' is unique
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the date when an item is created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically updates the date when an item is updated

    def __str__(self):
        return self.name
