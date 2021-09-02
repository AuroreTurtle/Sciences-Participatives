from django import forms
from web_site.models import Observation, Utilisateur, Especes, Admin
from django.contrib.admin.widgets import AdminDateWidget

class ObservationForm(forms.ModelForm):
	Date = forms.DateField(widget= forms.SelectDateWidget(years= range(2020, 2023)))
	class Meta:
		model = Observation
		fields = '__all__'
		
class UtilisateurForm(forms.ModelForm):
	class Meta:
		model = Utilisateur
		fields = '__all__'

class EspecesForm(forms.ModelForm):
	class Meta:
		model = Especes
		fields = '__all__'
class AdminForm(forms.ModelForm):
	class Meta:
		model = Admin
		fields = '__all__'
		
class 	ConnectionUtilisateurForm(forms.ModelForm):
		class Meta:
			model = Utilisateur
			fields = ['Login', 'Pwd']
			
class 	ConnectionAdminForm(forms.ModelForm):
		class Meta:
			model = Admin
			fields = ['Nom','N_matricule']

