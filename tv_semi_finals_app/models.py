from django.db import models
from datetime import datetime


class showsManger(models.Manager):

    def basic_validtor(self, post_date):
        errors = {}
        print(len(post_date['desc']))
        # add keys and values to errors dictionary for each invalid field
        if len(post_date['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(post_date['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(post_date['desc']) < 10 and len(post_date['desc']) != 0:
            errors["desc"] = "Description should be at least 10 characters"
        if datetime.today() < datetime.strptime(post_date['relase_date'], "%Y-%m-%d"):
            errors["relase_date"] = "Relase Date should be in the past"
        if shows.objects.filter(title=post_date['title']).exists():
            errors["title"] = 'Title Should be Uniqe Value'
        return errors

# @property
# def is_past_due(self):
#     return date.today() < self.date


class shows(models.Model):
    title = models.CharField(max_length=255, null=True)
    network = models.CharField(max_length=25, null=True)
    relase_date = models.DateField(null=True, auto_now_add=True)
    desc = models.TextField(null=True)

    objects = showsManger()

    def _create(title, network, relase_date, desc):
        shows.objects.create(title=title, network=network,
                             relase_date=relase_date, desc=desc)

    def _update(id, title, network, relase_date, desc):
        _show = shows.objects.get(id=id)
        _show.title = title
        _show.network = network
        _show.relase_date = relase_date
        _show.desc = desc
        _show.save()
