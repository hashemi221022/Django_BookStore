from django.contrib import admin
from .models import Book, Comment

# admin.site.register(Book)

# admin.site.register(Post, PostAdmin) #!ya in ya modele @admin.register(Comment) ghabele estefade ast
@admin.register(Book) #! estefade az in dastor bejaye = admin.site.register(Post, PostAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'price',) #! namayeshe ajza dar panele admin
    ordering = ('price', ) #! moratab kardane khodkar,,,,( '-status' = baraxs sort mikone)


# admin.site.register(Comment, CommentAdmin)  #! ya in ya modele @admin.register(Comment) ghabele estefade ast
@admin.register(Comment) #! ya az decorator estefade mikonim be in shekl
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_create', 'is_active', 'recommend')
    ordering = ('datetime_create',)




