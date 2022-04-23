from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import resolve_url


class BasePersonModel(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    born_at = models.DateField()

    def __str__(self):
        return self.name

    class Meta:             #tato classa se nenahraje do databaze, pokud by to tady nebylo, Actor se nezmeni a vytvori se nam dva modely BaseModel a Director => nechceme
        abstract = True



class Actor(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('actor_detail', pk=self.pk)


class Director(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('director_detail', pk=self.pk)


class Movie(models.Model): #automaticky dedi z models
    LANGUAGE_CHOICE_ENG = 'eng'     #ve velkych pismenech to znamena, ze je to konstanta
    LANGUAGE_CHOICE_CZ = 'cz'
    LANGUAGE_CHOICES = ((LANGUAGE_CHOICE_ENG, 'english'), (LANGUAGE_CHOICE_CZ, 'czech'),)

    name = models.CharField(max_length=256)
    description = models.TextField() #u textfield nemusime definovat max length
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    released = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='movies') #vrati nam vsechny filmy daneho herce
    director = models.ForeignKey(
        'Director',
        on_delete=models.SET_NULL,
        related_name='movies',
        null=True, blank=True) #on delete nam rika, co se stane s filmem, pokud smazeme toho rezisera
        #related_name klicove slovo, ktere pouzijeme pro iterovani
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}:{self.id}' #pomocna metoda, ktera nam misto objektu vypisuje rovnou jmeno filmu a ID

    def get_absolute_url(self):
        return resolve_url('movie_detail', pk=self.pk)


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.TextField()
    phone_number = models.IntegerField()
    contact_at = models.DateField()
