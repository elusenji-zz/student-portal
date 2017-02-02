from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ["title", "category", "created_date", "published_date"]

class CategoryAdmin(admin.ModelAdmin):
	def category_post_count(self, obj):
		return obj.post_set.count()
		
	prepopulated_fields = {'slug': ('title',)}
	list_display = ["title", "category_post_count"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
