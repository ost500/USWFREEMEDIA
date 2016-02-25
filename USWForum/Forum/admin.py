from django.contrib import admin

from Forum.models import Article, Category, Media


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content')
     
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Media)

# admin.site.register(Author)
# admin.site.register(Publisher)

# Register your models here.
