from django.contrib import admin

# Register your models here.
from .models import Donators
from .models import inNeed
from .models import Post

admin.site.register(Donators)
admin.site.register(inNeed)
admin.site.register(Post)