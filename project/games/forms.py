from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class GameForm(ModelForm):
    class Meta:
        model = models.Game
        fields = ('titre', 'studio', 'date_parution', 'synopsis', 'categorie')
        labels = {
        'titre': _('Titre'),
        'studio': _('Studio'),
        'date_parution': _('date de parution'),
        'synopsis': _('Synopsis'),
        'categorie': _('Catégorie')
        }


class Catform(ModelForm):
    class Meta :
        model = models.Categorie
        fields = ('nom', 'resume')
        labels = {
            'nom': _('Nom'),
            'resume': _('Résumé'),
        }
