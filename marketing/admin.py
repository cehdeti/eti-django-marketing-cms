from django.contrib import admin
from django.conf import settings
from .models import *

def make_published(modeladmin, request, queryset):
  queryset.update(page_status='p')
make_published.short_description = "Publish Selected Pages"

@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
	readonly_fields = ['last_updated']
	prepopulated_fields = {"slug": ["title"]}
	list_display = ['short_title', 'added_date', 'last_updated', 'page_status']
	list_filter = ['title', 'added_date', 'last_updated', 'page_status']
	search_fields = ['title']
	actions = [make_published]
	view_on_site = True

	fieldsets = (
		(None, {
			'fields': ('title', 'slug', 'last_updated', 'added_date',)
		}),
		('Header', {
			'fields': (('header', 'header_bg'), 'subheader', 'title_block',)
		}),
		('Layouts', {
			'fields': ('columns', 'column_1', 'column_2', 'sidebar', 'sidebar_text', 'footer')
		}),
		('Call to Actions', {
			'fields': ('cta', ('cta_text', 'cta_url'), 'socials',)
		}),
		('Additional SEO', {
			'classes': ('collapse',),
			'fields': ('seo_keywords', 'seo_description')
		}),
		('Page Status', { 'fields': ('page_status',) })
	)

	def get_changeform_initial_data(self, request):
		return {
			'cta_text': 'Contact Us'
		}