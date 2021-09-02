from django.shortcuts import render, redirect
from django.http import HttpResponse
from web_site.models import Observation, Utilisateur, Admin, Especes, Personnel_labo
from web_site.forms import ObservationForm, UtilisateurForm, AdminForm, EspecesForm, ConnectionUtilisateurForm, ConnectionAdminForm

#fonction pour la connexion d'un Utilisateur avec vérification de son login et de son mot de passe
def seconnecter(request):
	entree= ConnectionUtilisateurForm(request.POST or None)
	Log=entree.data.get("Login")
	Mdp=entree.data.get("Pwd")
	while Log is not None:
		try:
			User=Utilisateur.objects.get(Login=Log)
			if User.Pwd==Mdp:
				return redirect('page_home_utilisateur', utilisateur_id=User.id)
			else:
				return redirect ('page_erreur_login')
		except:
			return redirect ('page_erreur_login')
	return render(request,'connexion_utilisateur.html',{'entree':entree})


#fonction pour la création d'un compte Admin avec vérification de son matricule dans la base de données
def createAdminByForm (request):
	adm= Admin()
	perso_labo = Personnel_labo()
	form_adm = AdminForm(request.POST or None, instance=adm)
	entree_matrix=form_adm.data.get("N_matricule")
	entree_Nom= form_adm.data.get("Nom")
	while entree_matrix is not None:
		print(entree_Nom)
		try: 
			verif= Personnel_labo.objects.get(N_Matrix=entree_matrix)
			print(verif)
			if verif.Nom==entree_Nom:
				if form_adm.is_valid():
					adm.save()
					return redirect ('page_home_admin', admin_id=adm.id) 
				else:
					return render(request, 'creation_compte_admin.html', {'form': form_adm})
			else: 
				return redirect ('page_home')
		except:
			return redirect ('page_home')
	return render(request, 'creation_compte_admin.html', {'form': form_adm})


#fonction pour la connexion d'un Admin avec vérification de son matricule et de son Nom		
def seconnecterAdm(request):
	entreeAdm= ConnectionAdminForm(request.POST or None)
	Logadm=entreeAdm.data.get("Nom")
	x=entreeAdm.data.get("N_matricule")
	while Logadm is not None:
		try:
			Adm=Admin.objects.get(Nom=Logadm)
			print (x)
			if Adm.N_matricule==x:
				return redirect('page_home_admin', admin_id=Adm.id)
			else:
				return redirect ('page_home')
		except:
			return redirect ('page_erreur_login')
	return render(request,'connexion_admin.html',{'entreeAdm':entreeAdm})


#fonction pour afficher une page d'erreur
def erreur_login_utilisateur(request):
	return render(request, 'erreur_login_utilisateur.html', {})

	
def connexionTypes(request):
	return render(request, 'connexionTypes.html',{})


def home (request):
	return render (request, 'home.html', {})
# on avait mis le chemin en entier dans le settings.py d'où juste 'home' le nom


def entree_creer_compte (request):
	return render (request, 'entree_creer_compte.html', {})


#fonction pour le formulaire de création de compte Utilisateur
def createUtilisateurByForm (request):
	uti= Utilisateur()
	form_uti = UtilisateurForm(request.POST or None, request.FILES or None, instance=uti)
	if form_uti.is_valid():
		uti.save()
		return redirect ('page_home_utilisateur', utilisateur_id=uti.id) 
	else:
		return render(request, 'creation_compte_utilisateur.html', {'form': form_uti})
		

#fonction pour afficher sur la page home de l'Utilisateur toutes ses observations		
def home_utilisateur (request, utilisateur_id):
	try:
		utilisateur = Utilisateur.objects.get (id= utilisateur_id)
	except:
		return redirect ('page_home')
	observation= Observation.objects.all ()
	liste_observations = []
	for i in observation :
		if i.Observateur_id == utilisateur.id:
			liste_observations.append(i)
	return render (request, 'home_utilisateur.html', {'utilisateur': utilisateur, 'liste_observations' : liste_observations})
	 

#fonction pour afficher sur la page home de l'Admin toutes ses fiches Espèces
def home_admin (request, admin_id):
	try:
		admin = Admin.objects.get (id= admin_id)
	except:
		return redirect ('page_home')
	fiche= Especes.objects.all ()
	liste_fiche = []
	for i in fiche :
		if i.Auteur_fe_id == admin.id:
			liste_fiche.append(i)
	return render (request, 'home_admin.html', {'admin': admin, 'liste_fiche' : liste_fiche})


#fonction pour créer le formulaire pour créer la fiche Espèce
def createEspecesByForm (request):
	esp= Especes()
	form_esp = EspecesForm(request.POST or None, request.FILES or None, instance=esp)
	if form_esp.is_valid():
		esp.save()
		return redirect ('page_home') 
	else:
		return render(request, 'creation_especes.html', {'form': form_esp})


#fonction pour afficher toutes les données dans la fiche Espèce		
def  afficherFiche_especes(request, especes_id):
	try:
		especes = Especes.objects.get(id=especes_id) 
	except:
		#        return render(request, 'application_sciences_participatives/no_data.html') #sinon on affiche une page d'erreur
		liste_espece=Especes.objects.all()
	return render(request,'fiche_especes.html',{'especes':especes})


#fonction pour afficher la page de la liste des especes observees
def especes(request): 
    especes=Especes.objects.all()#On récupère les espèces existantes..
    especes_plantes=[] #liste des especes végétales
    especes_champignons=[] #liste des especes de champignons
    especes_insectes=[] #liste des especes insectes
    especes_mammiferes=[] #liste des especes de mammiferes
    especes_reptiles_amphibiens=[] #liste des especes de reptiles et amphibiens
    especes_oiseaux=[] #liste des especes oiseaux
    especes_autres=[] #liste des autres especes
    for i in especes:#Dans la liste des especes existantes
        if i.Categorie_especes==1: # si c'est categorie plantes
            especes_plantes.append(i)#on les ajoute dans la liste des espèces de plantes
        elif i.Categorie_especes==2: # si c'est categorie champignons
            especes_champignons.append(i) #on les ajoute dans la liste des champignons
        elif i.Categorie_especes==3: #si c'est categorie insectes
            especes_insectes.append(i) #on les ajoute dans la liste des insectes
        elif i.Categorie_especes==4: #si c'est categorie reptiles et amphibiens
            especes_reptiles_amphibiens.append(i) #on les ajoute dans la liste des espèces de reptiles et amphibiens
        elif i.Categorie_especes==5: #si c'est categorie mammifères
            especes_mammiferes.append(i) #on les ajoute dans la liste des espèces de mammiferes
        elif i.Categorie_especes==6: #si c'est categorie oiseaux
            especes_oiseaux.append(i) #on les ajoute dans la liste des espèces des oiseaux
        else: #si c'est autre choses qui n'est pas mentionnée en haut
            especes_autres.append(i) #on les ajoute dans la liste des autres catégorie d' espèces
    return render(request,'liste_fiches_especes.html',{'especes_plantes':especes_plantes, 'especes_champignons':especes_champignons,'especes_insectes':especes_insectes, 'especes_reptiles_amphibiens':especes_reptiles_amphibiens, 'especes_mammiferes':especes_mammiferes, 'especes_oiseaux':especes_oiseaux, 'especes_autres':especes_autres})


#fonction pour éditer la fiche espèce
def editerEspece (request, pk_id):
	try:
		ficheEditer = Especes.objects.get(id=pk_id)
	except:
		return render (request, 'erreur.html')
	ficheEditer_form = EspecesForm(request.POST or None, request.FILES or None, instance=ficheEditer)
	if ficheEditer_form.is_valid():
		ficheEditer_form.save()
		return redirect('page_liste_especes')
	else:
		return render (request, 'editer_espece.html', {'ficheEditer_form': ficheEditer_form, 'ficheEditer' : ficheEditer, 'id':pk_id}) 
	

#fonction pour créer le formulaire pour l'observation	
def createObservationByForm (request):
	obs= Observation()
	form_obs = ObservationForm(request.POST or None, request.FILES,  instance=obs)
	if form_obs.is_valid():
		obs.save()
		return redirect ('page_home')
	else:
		return render(request, 'creation_observation.html', {'form': form_obs})


#fonction pour afficher toutes les observations des utilisateurs	
def afficher_observations(request): 
    afficher_obs=Observation.objects.all()#On récupère les espèces existantes..
    return render(request,'liste_observations.html', {'afficher_obs': afficher_obs})
    
    
#fonction pour afficher toutes les données d'une observation	
def afficherObservation(request, obs_id):
    try:
        obs = Observation.objects.get(id=obs_id)
    except:
        return render (request, 'erreur.html')
        
        liste_obs=Observation.objects.all()
    return render(request,'fiche_observation.html',{'obs':obs})

   
def contact (request):
	return render (request, 'contact.html', {})