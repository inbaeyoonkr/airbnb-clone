from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Model Review Definition """

    review = models.TextField()
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    accuracy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    check_in = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.cleanliness
            + self.accuracy
            + self.communication
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg"

    class Meta:
        ordering = ("-created",)

