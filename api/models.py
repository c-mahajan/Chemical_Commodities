from django.db import models
from django.db.models.signals import m2m_changed
from django.core.validators import MaxValueValidator
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your models here.

class Chemical(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"

class ChemCompo(models.Model):
    element = models.ForeignKey(Chemical, on_delete=models.CASCADE, related_name='compositions')
    percentage = models.FloatField(validators=[MaxValueValidator(100, message="The Chemical composition percentage is wrong.")])

    def __str__(self):
        return f"{self.id} - {self.element} - {self.percentage} %"

class Commodity(models.Model):
    name = models.CharField(max_length=200)
    inventory = models.FloatField()
    price = models.FloatField()
    chemical_composition = models.ManyToManyField(ChemCompo, related_name='commodities')

    def __str__(self):
        return f"{self.id} - {self.name}"

def save_commodity_model_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add':
        total = 0
        # print(instance.chemical_composition.all())
        for chem in instance.chemical_composition.all():
            # print(chem.percentage)
            total += chem.percentage

        # print(total)
        unknown = Chemical.objects.get(name = 'Unknown')
        if total < 100:
            unknown_percentage = 100 - total
            unknown_object = ChemCompo.objects.create(element = unknown, percentage=unknown_percentage)
            # print(unknown_object)
            instance.chemical_composition.add(unknown_object)
            instance.save()
        elif total > 100:
            per = total - 100
            unknown_percentage = instance.chemical_composition.get(element=unknown).percentage
            # print(unknown_percentage)
            if unknown_percentage == per:
                unknwn = instance.chemical_composition.get(element=unknown)
                instance.chemical_composition.remove(unknwn)
                instance.save()
            elif unknown_percentage < per:
                # print("Error")
                raise ValueError("Invalid Chemical Composition.")
            elif unknown_percentage > per:
                final = unknown_percentage - per
                un_ele = instance.chemical_composition.get(element=unknown)
                un_ele.percentage = final
                un_ele.save()
                # print("Final:",instance.chemical_composition.get(element=unknown).percentage)
                instance.save()
        else:
            instance.save()
    elif action == 'post_remove':
        total = 0
        # print(instance.chemical_composition.all())
        for chem in instance.chemical_composition.all():
            # print(chem.percentage)
            total += chem.percentage

        print("IN POST_REMOVE:",total)
        unknown = Chemical.objects.get(name = 'Unknown')
        if total < 100:
            unknown_percentage = 100 - total
            # print(unknown_percentage)
            if_unknown = list(filter(lambda x: x.element == unknown, instance.chemical_composition.all()))
            if if_unknown:
                un_ele = instance.chemical_composition.get(element=unknown)
                un_ele.percentage += unknown_percentage
                un_ele.save()
            else:
                # print("In Post Rem Else")
                unknown_object = ChemCompo.objects.create(element = unknown, percentage=unknown_percentage)
                # print(unknown_object)
                instance.chemical_composition.add(unknown_object)
                instance.save()

m2m_changed.connect(save_commodity_model_receiver, sender = Commodity.chemical_composition.through)
