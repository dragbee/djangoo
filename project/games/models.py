from django.db import models

# Create your models here.

class Game(models.Model):
    titre = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    synopsis = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, null=True)

    def __str__(self):
        chaine = f"{self.titre} | {self.studio} | {self.date_parution} | Catégorie : {self.categorie}"
        return chaine

    def dico(self):
        return {"titre":self.titre, "studio":self.studio, "date_parution":self.date_parution, "synopsis":self.synopsis, "categorie": self.categorie}


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine2 = f"{self.nom} | {self.resume}"
        return chaine2

    def dico(self):
        return {"nom":self.nom, "resume":self.resume}
