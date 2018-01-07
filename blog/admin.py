from django.contrib import admin
# Register your models here.

# importing Post model from './models.py' file
from .models import Post

admin.site.register(Post)
