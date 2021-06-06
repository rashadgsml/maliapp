from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import Contract,Person,JuridicalPerson,IndividualPerson
from .serializers import ContractSerializer, JuridicalPersonSerializer, IndividualPersonSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from django.http import Http404
from .permissions import IsOwner
from .utils import update_contract_number, create_person
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ContractsView(APIView):

    permission_classes = (IsAuthenticated, IsOwner,)
    serializer_class = ContractSerializer

    
    def get(self, request, *args, **kwargs):
        queryset = Contract.objects.filter(user=request.user)
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)
        
    @swagger_auto_schema(request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['region'],
                             properties={
                                 'region': openapi.Schema(type=openapi.TYPE_STRING)
                             },
                         ),
                         operation_description='Description')
    def post(self, request, *args, **kwargs):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.validated_data['user'] = request.user
            customer, seller = create_person(request.data)
            serializer.validated_data['seller'] = seller
            serializer.validated_data['customer'] = customer
            
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ContractDetail(APIView):

    permission_classes = (IsAuthenticated, IsOwner,)

    def get_object(self, pk):
        try:
            return Contract.objects.get(pk=pk)
        except Contract.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Contract = self.get_object(pk)
        serializer = ContractSerializer(Contract)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Contract = self.get_object(pk)
        serializer = ContractSerializer(Contract, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contract = self.get_object(pk)
        contract.delete()

        Contract.objects.filter(user=request.user).update(contract_number=0)
        contracts = Contract.objects.filter(user=request.user).order_by('timestamp')

        update_contract_number(contracts)
        return Response(status=HTTP_204_NO_CONTENT)
