from rest_framework.serializers import ModelSerializer
from .models import Chemical, ChemCompo, Commodity

class ChemicalSerializer(ModelSerializer):
    class Meta:
        model = Chemical
        fields = '__all__'

class ChemCompoSerializer(ModelSerializer):
    element = ChemicalSerializer()
    class Meta:
        model = ChemCompo
        fields = ('id','element', 'percentage')

class CommoditySerializer(ModelSerializer):
    # chemicals = ChemicalSerializer(many = True)
    chemical_composition = ChemCompoSerializer(many = True)
    class Meta:
        model = Commodity
        fields = ('id', 'name', 'price', 'inventory', 'chemical_composition')
    