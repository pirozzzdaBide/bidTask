from django.db import models

class Category(models.Model):
    text = models.CharField(max_length=150)
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'categories'

class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='meh')
    text = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
