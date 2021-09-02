from django.db import models
from datetime import datetime

class Personnel_labo(models.Model):
	Nom = models.CharField(max_length=50)
	Prenom = models.CharField(max_length=25,  verbose_name = "Prénom")
	Email = models.CharField(max_length=100, verbose_name = "Adresse é-mail")
	Fonction = models.IntegerField(verbose_name= "Fonction", choices =[(1, ("Botaniste")), (2, ("Directeur")), (3, ("Ecologiste")), (4, ("Paleontologue")), (5, ("Informaticien")), (6, ("Ornithologue")), (7, ("Entomologiste")), (8, ("Autre"))], default=8)
	N_Matrix = models.CharField(max_length=25, null=False, verbose_name = "N° matricule")
	class Meta:
		verbose_name = "Personnel_labo"
		ordering = ['Nom']
	def __str__(self):
		return self.Fonction

class Utilisateur(models.Model):
	Nom = models.CharField(max_length=50)
	Prenom = models.CharField(max_length=25,  verbose_name = "Prénom")
	Photo = models.ImageField(upload_to='media/', verbose_name = "Votre photo de profil")
	Email = models.CharField(max_length=100, verbose_name = "Adresse é-mail")
	Login = models.CharField(max_length=100, verbose_name = "Votre login")
	Pwd = models.CharField(max_length=100, verbose_name = "Votre mot de passe")
	class Meta:
		verbose_name = "Utilisateur"
		ordering = ['Nom']
	def __str__(self):
		return self.Login
		
class Admin(models.Model):
	Nom = models.CharField(max_length=50)
	Prenom = models.CharField(max_length=25,  verbose_name = "Prénom")
	N_matricule= models.CharField(max_length=25, null=False, verbose_name = "N° matricule") #obligé de mettre en CharField sinon connexion avec InterField ça fonctionne pas
	Personnel =models.ForeignKey(Personnel_labo, on_delete = models.CASCADE, verbose_name= "Fonction")

	class Meta:
		verbose_name = "Admin"
		ordering = ['Nom']
	def __str__(self):
		return self.Prenom
		
class Especes(models.Model):
	Nom_vernaculaire = models.CharField(max_length=150, verbose_name = "Nom commun")
	Familles = models.CharField(max_length=100)
	Ordre = models.CharField(max_length=100)
	Nom_scientifiques= models.CharField(max_length=150, null= False, unique = True, verbose_name = "Nom scientifique")
	Photo = models.ImageField(upload_to='media/', verbose_name = "Ajouter une photo")
	Description = models.TextField()
	Repartition_geographique = models.CharField(max_length=150, verbose_name = "Répartition géographique")
	TaxRef = models.CharField(max_length=150)
	Habitat = models.CharField(max_length=100, verbose_name = "Types d'habitat naturel")
	Statut_IUCN = models.CharField(max_length=100, verbose_name = "Statut de conservation UICN")
	Categorie_especes = models.IntegerField(verbose_name= "Catégorie de l'espèce", choices =[(1, ("Plantes")), (2, ("Champignons")), (3, ("Insectes")), (4, ("Reptiles et Amphibiens")), (5, ("Mammifères")), (6, ("Oiseaux"))])
	Auteur_fe = models.ForeignKey(Admin, on_delete = models.CASCADE, verbose_name = "Auteur fiche espèce")
	
	class Meta:
		verbose_name = "Especes"
		ordering = ['Familles']
	def __str__(self):
		return self.Nom_vernaculaire

class Observation(models.Model):
	Ville = models.CharField(max_length=150, null= False, verbose_name = "Ville d'observation")
	Departement = models.CharField(max_length=150, verbose_name = "Département d'observation")
	Pays = models.CharField(max_length=150, null= False, verbose_name = "Pays")
	Date = models.DateTimeField(default=datetime.now, verbose_name="Date d'observation")
	Photos= models.ImageField(upload_to='media/', verbose_name = "Ajouter une photo")
	Estimation = models.IntegerField(default=1, verbose_name = "Estimation du nombre d'individu")
	Observateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null= False)
	sp_observe = models.ForeignKey(Especes, on_delete = models.CASCADE, null= False, verbose_name = "Espèce observée")
	class Meta:
		verbose_name = "Observation"
		ordering = ['Departement']

# Create your models here.
