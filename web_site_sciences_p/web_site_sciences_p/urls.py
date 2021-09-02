"""web_site_sciences_p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_site.views import home, createUtilisateurByForm, createObservationByForm, createAdminByForm, createEspecesByForm, afficherFiche_especes, especes, home_utilisateur
from web_site.views import home_admin, editerEspece, erreur_login_utilisateur, seconnecter, afficher_observations, entree_creer_compte
from web_site.views import connexionTypes, seconnecterAdm, afficherObservation, contact
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home' , home, name='page_home'), 
    path('create/utilisateur', createUtilisateurByForm, name= 'page_creer_compte_utilisateur'),
    path('create/admin' , createAdminByForm, name = 'page_creer_compte_admin'),
    path('create/especes' , createEspecesByForm, name = 'page_creer_especes'),
    path('create/observation', createObservationByForm, name= 'page_creer_observation'),
    path('affiche/especes/<int:especes_id>', afficherFiche_especes, name = 'page_fiche_especes'), 
    path('liste/especes', especes, name = 'page_liste_especes'),
    path('home/utilisateur/<int:utilisateur_id>', home_utilisateur, name = 'page_home_utilisateur'),
    path('home/admin/<int:admin_id>', home_admin, name= 'page_home_admin'),
    path('fiche/editer/<int:pk_id>', editerEspece, name = 'page_editer_especes'),
    path('erreur/login', erreur_login_utilisateur, name = 'page_erreur_login'),
    path('connexion/utilisateur',seconnecter, name= 'page_connexion_utilisateur'),  
    path('liste/observation', afficher_observations, name='page_liste_observations'),
    path('entree/compte', entree_creer_compte, name='page_entree_creer_compte'),
    path('connexion/types', connexionTypes, name = 'page_connexionTypes'),
    path('connexion/admin',seconnecterAdm, name= 'page_connexion_admin'),
    path('affiche/observation/<int:obs_id>', afficherObservation, name = 'page_fiche_observation'),
    path('contact' , contact, name='page_contact'),
    path('accounts/', include('django.contrib.auth.urls')), # new
    
]

# afin d'avoir le lien des photos qui sont chargées et les afficher après 
if settings.DEBUG is True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
