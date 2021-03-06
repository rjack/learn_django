from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


# You'll follow this pattern -- create a model admin object, then pass it as
# the second argument to admin.site.register() -- any time you need to change
# the admin options for an object.
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_today')
	list_filter = ['pub_date']
	search_fields = ['questions']
	date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
