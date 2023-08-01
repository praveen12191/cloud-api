from rest_framework.serializers import ModelSerializer
from .models import Items

class ItemSerializer(ModelSerializer):
    class Meta:
        model =  Items 
        fields = '__all__'


