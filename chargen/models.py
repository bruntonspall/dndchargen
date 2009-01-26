from django.db import models

def attribute_bonus(self, value):
    """ Returns the bonus that an attribute at this level gives you """
    """ 
    >>> attribute_bonus(9)
    -1
    >>> attribute_bonus(10)
    0
    >>> attribute_bonus(15)
    2
    """
    #1 = -6 + (2 / 2) + (2 % 2) = -6 + 1 + 0 = -5
    #2 = -6 + (3 / 2) + (3 % 2) = -6 + 1 + 1 = -4
    return -1 + -5 + ((value+1)/2)+((value+1)%2)
    
RACES = (
('S', 'Small'),
('M', 'Medium'),
('L', 'Large')
)
VISIONS = (
('N', 'Normal'),
('L', 'Low Light'),
('D', 'Dark vision'),
)

POWER_USE = (
('W', 'At Will'),
('E', 'Encounter'),
('D', 'Daily'),
)

class Language(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name
        
class Skill(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name
        
class WeaponProficiences(models.Model):
    name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name
        
class Power(models.Model):
    name = models.CharField(max_length=32)
    use_type = models.CharField(max_length=1, choices=POWER_USE)
    

     
class Race(models.Model):
    name = models.CharField(max_length=32)
    str_bonus = models.IntegerField()
    con_bonus = models.IntegerField()
    dex_bonus = models.IntegerField()
    int_bonus = models.IntegerField()
    wis_bonus = models.IntegerField()
    chr_bonus = models.IntegerField()
    floating_bonus = models.IntegerField()
    size = models.CharField(max_length=2, choices=RACES)
    walk_speed = models.IntegerField()
    fly_speed = models.IntegerField()
    teleport_speed = models.IntegerField()
    vision = models.CharField(max_length=2, choices=VISIONS)
    languages = models.ManyToManyField(Language)
    skill_bonuses = models.ManyToManyField(Skill)
    ac_bonus = models.IntegerField()
    ref_bonus = models.IntegerField()
    for_bonus = models.IntegerField()
    will_bonus = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
    
ALIGN_CHOICES = (
        ('LG', 'Lawful Good'),
        ('G', 'Good'),
        ('N', 'Neutral'),
        ('E', 'Evil'),
        ('CE', 'Chaotic Evil'),
    )

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=32)
    # Core Attributes
    strength = models.IntegerField()
    constitution = models.IntegerField()
    dexterity = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    
    alignment = models.CharField(max_length=2, choices=ALIGN_CHOICES)
    diety = models.CharField(max_length=32)
    home_region = models.CharField(max_length=32)
    
    
    def __unicode__(self):
        return self.name
