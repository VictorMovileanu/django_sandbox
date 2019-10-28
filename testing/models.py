from django.db import models
from django_extensions.db.models import TimeStampedModel


class Profile(TimeStampedModel):
    """
    mock data schema: https://mockaroo.com/f6ef5340
    """
    first_name = models.CharField(verbose_name="First name", help_text="First name", max_length=100)
    last_name = models.CharField(verbose_name="Last name", help_text="Last name", max_length=100)
    email = models.EmailField(verbose_name="E-Mail", help_text="E-Mail", max_length=100)


class Event(TimeStampedModel):
    """
    mock data schema: https://mockaroo.com/61f36320
    """
    name = models.CharField(verbose_name="Event name", help_text="Event name", max_length=100)
    price = models.DecimalField(verbose_name="Price", help_text="Price payed for the event", decimal_places=2,
                                max_digits=5)
    person = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="events")
