from rest_framework import serializers
from contracts.models import Contract, Person, JuridicalPerson, IndividualPerson
from users.api.serializers import UserSerializer

class ContractSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    
    class Meta:
        model = Contract
        fields = ('id', 'contract_number', 'region','timestamp','user','seller','customer')
        extra_kwargs={
            "region":{"required":True},
            "seller":{"required":True},
            "customer":{"required":True},
        }
    
    def get_user(self,obj):
        return UserSerializer(obj.user).data

    def get_seller(self, obj):
        return PersonSerializer(obj.seller).data
    
    def get_customer(self, obj):
        return PersonSerializer(obj.customer).data
        


class PersonSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = ('person',)
    
    def get_person(self,obj):
        try:
            return JuridicalPersonSerializer(obj.person).data
        except:
            return IndividualPersonSerializer(obj.person).data

class JuridicalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuridicalPerson
        fields = ('name','surname','voen','organization_name','organization_address',)

class IndividualPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualPerson
        fields = ('name','surname','voen','identity_number','given_date','given_organization_name',)