from django.contrib import admin
from .models import Post, Comment, Detail, ProfileImage

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Detail)
admin.site.register(ProfileImage)
# admin.site.register(Detail, CustomUserAdmin)