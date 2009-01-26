from django.contrib import admin
from DnDCharGen.chargen.models import Language, Race, Character, Skill, WeaponProficiences

class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class RaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Race, RaceAdmin)

class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)

class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)

class WeaponProficiencesAdmin(admin.ModelAdmin):
    pass
admin.site.register(WeaponProficiences, WeaponProficiencesAdmin)
