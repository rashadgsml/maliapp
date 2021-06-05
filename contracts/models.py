from django.db import models
from django.conf import settings

class Contract(models.Model):
    contract_number = models.IntegerField(blank=True, null=True,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey('Person',related_name='seller',on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey('Person',related_name='customer',on_delete=models.CASCADE, blank=True, null=True)
    region = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            self.contract_number = max((Contract.objects.filter(user=self.user).values_list('contract_number', flat=True))) + 1
        except:
            # Contract.objects.filter(user=self.user).update(contract_number=0)
            self.contract_number = 1

        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.contract_number)

class Person(models.Model):
    juridical_person = models.ForeignKey('JuridicalPerson', on_delete=models.CASCADE, blank=True, null=True)
    individual_person = models.ForeignKey('IndividualPerson', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def person(self):
        if self.juridical_person:
            return self.juridical_person
        return self.individual_person

    def __str__(self):
        return self.person.name

class JuridicalPerson(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    voen = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=50)
    organization_address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class IndividualPerson(models.Model):
    name  = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    voen = models.CharField(max_length=50)
    identity_number = models.PositiveIntegerField()
    given_date = models.DateTimeField()
    given_organization_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name