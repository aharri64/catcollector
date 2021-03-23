from django.db import models

# Create your models here.


class Cat(models.Model):
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# garfield = Cat('Garfield', 'Tabby', 'I have never heard of Tabby', 9)
# print(garfield)


# done on 3/23/2021
# Tuples (value1, value2, value3) They are immutable pop() no changing of the values.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Feeding(models.Model):
    date = models.DateField('when are we getting fed')
    meal = models.CharField(
        max_length=1,
        # possible choices are meals
        choices=MEALS,
        default=MEALS[0][0]
    )
    # mmake association to Cat Model, when cat is deleted, delete associated feedings
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
