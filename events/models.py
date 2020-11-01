from django.db import models

class Event_Type(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'event_type'
        verbose_name_plural = 'event_types'

    def __str__(self):
        return self.name

class Event(models.Model):
    event_type = models.ForeignKey(Event_Type,
                                related_name='events',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, db_index=True)
    slug = models.SlugField(max_length = 200, db_index=True)
    image = models.ImageField(upload_to='gallery/%Y/%m', blank=True)
    description = models.TextField(blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    whatsapp_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    event_link = models.URLField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        #for queries involving id and slug

    def __str__(self):
        return self.name
