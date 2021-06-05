from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','user_name','first_name','last_name','company_name',
                        'company_address','start_date','is_staff','is_active',)