from django import forms
from django.db import IntegrityError
from django.utils.text import slugify

from .models import Action


class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        exclude = ('slug',)

    def clean(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug', '')
        if not slug:
            slug = slugify(self.cleaned_data['name'])

        self.cleaned_data['slug'] = slug
        return super(ActionForm, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        base_slug = self.cleaned_data.get('slug', '')
        iteration = 0
        while True:
            try:
                return super(ActionForm, self).save(*args, **kwargs)
            except IntegrityError:
                iteration += 1
                self.instance.slug = '{}-{}'.format(base_slug, iteration)
