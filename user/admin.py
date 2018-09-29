from django.contrib import admin
from user.models import User

# admin.site.register([User])

# class
# class UserAdmiin(admin,ModelAdmin):
#     fields = ('nickName')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('account','password','phone','email','nickName','createDate','editDate')
    search_fields = ('account','password','phone','email','nickName','createDate','editDate')
