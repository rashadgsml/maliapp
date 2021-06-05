from django.contrib import admin
from .models import Contract, Person, JuridicalPerson, IndividualPerson

admin.site.register(Contract)
admin.site.register(Person)
admin.site.register(JuridicalPerson)
admin.site.register(IndividualPerson)
