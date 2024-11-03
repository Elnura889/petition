from django.contrib import admin
from .models import Petition, Vote

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'vote_count')
    search_fields = ('title',)
    ordering = ('-created_at',)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'petition', 'created_at')
    list_filter = ('petition',)
    ordering = ('-created_at',)

# Registering the models with the admin site
admin.site.register(Petition, PetitionAdmin)
admin.site.register(Vote, VoteAdmin)

