from ..models import JuridicalPerson, IndividualPerson, Person
from rest_framework.response import Response

def update_contract_number(contracts):
    for i in contracts:
        i.save()

def create_person(data):
    try:
        if data['customer']['person']['type'] == 'huquqi':
            customer_type = JuridicalPerson.objects.create(name=data['customer']['person']['name'],
                                            surname=data['customer']['person']['surname'],
                                            voen=data['customer']['person']['voen'],
                                            organization_name=data['customer']['person']['organization_name'],
                                            organization_address=data['customer']['person']['organization_address'])
            customer = Person.objects.create(juridical_person=customer_type)
            
        else:
            customer_type = IndividualPerson.objects.create(name=data['customer']['name'],
                                        surname=data['customer']['person']['surname'],
                                        voen=data['customer']['person']['voen'],
                                        identity_number=data['customer']['person']['identity_number'],
                                        given_date=data['customer']['person']['given_date'],
                                        given_organization_name=data['customer']['person']['given_organization_name'],
            )
            customer = Person.objects.create(individual_person=customer_type)

        if data['seller']['person']['type'] == 'huquqi':
            seller_type = JuridicalPerson.objects.create(name=data['seller']['person']['name'],
                    surname=data['seller']['person']['surname'],
                    voen=data['seller']['person']['voen'],
                    organization_name=data['seller']['person']['organization_name'],
                    organization_address=data['seller']['person']['organization_address'])
            seller = Person.objects.create(juridical_person=seller_type)
        
        else:
            seller_type = IndividualPerson.objects.create(name=data['seller']['person']['name'],
                surname=data['seller']['person']['surname'],
                voen=data['seller']['person']['voen'],
                identity_number=data['seller']['person']['identity_number'],
                given_date=data['seller']['person']['given_date'],
                given_organization_name=data['seller']['person']['given_organization_name'],
            )
            seller = Person.objects.create(individual_person=customer_type)
        
        return customer, seller
    except:
        return Response("You might missed some fields.")