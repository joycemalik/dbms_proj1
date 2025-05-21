from django.db import models

class Severity(models.Model):
    severity_id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=50)

class DisasterType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    response_time = models.IntegerField()
    frequency = models.IntegerField()

class Cause(models.Model):
    cause_id = models.AutoField(primary_key=True)
    primary_cause = models.CharField(max_length=255)
    secondary_cause = models.CharField(max_length=255, blank=True, null=True)

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    area = models.IntegerField()

class Disaster(models.Model):
    disaster_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    confirmation = models.BooleanField(default=False)
    duration = models.IntegerField()
    type = models.ForeignKey(DisasterType, on_delete=models.CASCADE)
    severity = models.ForeignKey(Severity, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    locations = models.ManyToManyField(Location, through='DisasterLocation')

class DisasterLocation(models.Model):
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('disaster', 'location')

class Impact(models.Model):
    impact_id = models.AutoField(primary_key=True)
    evacuated = models.IntegerField()
    injured = models.IntegerField()
    death = models.IntegerField()
    ecology = models.CharField(max_length=255)
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)

class RecoveryShelter(models.Model):
    shelter_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    area = models.IntegerField()
    cost = models.IntegerField()
    capacity = models.IntegerField()
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Organisation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    class Meta:
        unique_together = ('location', 'name')

class Aid(models.Model):
    aid_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE)
