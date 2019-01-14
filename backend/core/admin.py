from django.contrib import admin
from .models import Test, User,Place,Photo

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Test)
admin.site.register(Photo)