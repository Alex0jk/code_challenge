# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import JSONField

class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_client = models.ForeignKey('Client', models.DO_NOTHING, db_column='id_client')
    details_order = JSONField()
    price_order = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ORDER'


class Client(models.Model):
    id_client = models.CharField(primary_key=True, max_length=10)
    name_client = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'client'


class Ingredient(models.Model):
    id_ingredient = models.AutoField(primary_key=True)
    name_ingredient = models.CharField(max_length=50)
    price_ingredient = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ingredient'


class Size(models.Model):
    id_size = models.AutoField(primary_key=True)
    name_size = models.CharField(max_length=50)
    price_size = models.FloatField()

    class Meta:
        managed = False
        db_table = 'size'
