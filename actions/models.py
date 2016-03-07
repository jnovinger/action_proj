from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, blank=False, unique=True)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    due = models.DateField(null=True, blank=True)
    completed = models.DateTimeField(null=True, blank=True)

    assigned_to = models.ForeignKey('auth.User',
                                    related_name='assigned_actions')
    assigned_on = models.DateTimeField(null=True, blank=True)

    deleted = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('action-detail', kwargs={'pk': self.id})
    absolute_url = property(get_absolute_url)

    def get_assigned_to(self):
        """Provide fallback for `assigned_to` repr"""
        assigned_to = self.assigned_to
        full_name = assigned_to.get_full_name()
        if full_name:
            return full_name

        return str(assigned_to)
    assigned_to_pretty = property(get_assigned_to)



# ActionHistory?
