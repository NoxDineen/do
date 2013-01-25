from django.contrib import admin
from models import Player, Story, Letter, GoalWord


class PlayerAdmin(admin.ModelAdmin):
	pass
admin.site.register(Player, PlayerAdmin)


class StoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Story, StoryAdmin)


class LetterAdmin(admin.ModelAdmin):
	pass
admin.site.register(Letter, LetterAdmin)


class GoalWordAdmin(admin.ModelAdmin):
	pass
admin.site.register(GoalWord, GoalWordAdmin)
