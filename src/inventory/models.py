from django.conf import settings
from django.db import models


class DataHubLegacyUser(models.Model):

    """DataHub's old User model. Replaced by the Django User model."""

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    f_name = models.CharField(max_length=50, null=True)
    l_name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "datahub_legacy_users"


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    repo_base = models.CharField(max_length=50)
    repo_name = models.CharField(max_length=50)
    card_name = models.CharField(max_length=50)
    query = models.TextField()

    def __unicode__(self):
        return 'card: %s.%s %s' % (self.repo_base,
                                   self.repo_name, self.card_name)

    class Meta:
        db_table = "cards"
        unique_together = ('repo_base', 'repo_name', 'card_name')


class Annotation(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    url_path = models.CharField(max_length=500, unique=True)
    annotation_text = models.TextField()

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "annotations"


class App(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    app_id = models.CharField(max_length=100, unique=True)
    app_name = models.CharField(max_length=100)
    app_token = models.CharField(max_length=500)
    legacy_user = models.ForeignKey('DataHubLegacyUser', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    def __unicode__(self):
        return self.app_name

    class Meta:
        db_table = "apps"


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    legacy_user = models.ForeignKey('DataHubLegacyUser', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    app = models.ForeignKey('App')
    access = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "permissions"
        

class Collaborator (models.Model):
  id = models.AutoField(primary_key=True)
  timestamp = models.DateTimeField(auto_now=True)
  legacy_user = models.ForeignKey('DataHubLegacyUser', null=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
  repo_name = models.CharField(max_length=50)
  repo_owner = models.CharField(max_length=50)
  permission = models.CharField(max_length=50)

  def __unicode__ (self):
    return self.id

  class Meta:
    db_table = "collaborators"
