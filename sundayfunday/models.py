from django.contrib.auth import models as auth_models
from django.db import models

class User(auth_models.AbstractUser):
    """User that can login/logout + his type."""
    USER = 1
    ORGANISER = 2

    TYPES = (
        (USER, 'USER'),
        (ORGANISER, 'ORGANISER'),
        # TODO Add Admin if needed
    )

    user_type = models.IntegerField(choices=TYPES, default=USER)
    preference = models.ManyToManyField('Preference', blank=True)

    @property
    def name(self):
        return ' '.join([self.first_name.capitalize(),
                         self.last_name.capitalize()])


class Event(models.Model):
    """Event in our DB."""

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey('User')
    preference = models.ManyToManyField('Preference', blank=True)

    def __str__(self):
        return self.title

class Preference(models.Model):
    """ default preferences"""

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Comment(models.Model):
    """ comments for events"""

    comment = models.CharField(max_length=10000)
    date = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s" % self.id

class Grade(models.Model):
    """ event grading"""

    user = models.ForeignKey('User')
    event = models.ForeignKey('Event')

    TYPES = (
        (1, "POOR"),
        (2, "FAIR"),
        (3, "AVERAGE"),
        (4, "GOOD"),
        (5, "EXCELLENT"),
    )
    grade = models.IntegerField(choices=TYPES, default=5)

    def __str__(self):
        return "%s" % self.id

class Friend(models.Model):
    """ friending"""

    first_person = models.ForeignKey('User', related_name='person1')
    second_person = models.ForeignKey('User', related_name='person2')
    date = models.DateTimeField()

    def __str__(self):
        return "%s" % self.id
