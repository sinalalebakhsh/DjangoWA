from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'status', 'date_time_created', 'date_time_modified')
    ordering = ('date_time_created', )

# admin.site.register(Post, PostAdmin)



