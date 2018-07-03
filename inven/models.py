from django.db import models


class ProviderDataset(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProviderAttribute(models.Model):
    dataset = models.ForeignKey(ProviderDataset, on_delete=models.CASCADE)
    table = models.CharField(max_length=128)
    field = models.CharField(max_length=128)
    entity = models.CharField(max_length=128)
    attribute = models.CharField(max_length=128)

    def __str__(self):
        return self.dataset + ' / ' + self.entity + '.' + self.attribute


class ConsumerAttribute(models.Model):
    entity = models.CharField(max_length=128)
    attribute = models.CharField(max_length=128)

    def __str__(self):
        return self.entity + '.' + self.attribute


class Entity(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=128)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return self.entity.name + '.' + self.name
