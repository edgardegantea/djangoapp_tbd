from django.db import models
from django.db.models.functions import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(verbose_name="Pregunta", max_length=150)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return "Votos: {0} - Pregunta: {1}".format(self.votes, self.question)

    class Meta:
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'
