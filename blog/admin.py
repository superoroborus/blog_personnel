from django.contrib import admin
# Importation du module admin de Django pour enregistrer les modèles dans l'interface d'administration

# Register your models here.
# Enregistrez vos modèles ici.

from blog.models import Category, Comment, Post
# Importation des modèles Category, Comment et Post depuis blog.models

class CategoryAdmin(admin.ModelAdmin):
    # Classe d'administration pour le modèle Category
    pass
    # Utilisation de la configuration par défaut de ModelAdmin

class PostAdmin(admin.ModelAdmin):
    # Classe d'administration pour le modèle Post
    pass
    # Utilisation de la configuration par défaut de ModelAdmin

class CommentAdmin(admin.ModelAdmin):
    # Classe d'administration pour le modèle Comment
    pass
    # Utilisation de la configuration par défaut de ModelAdmin

admin.site.register(Category, CategoryAdmin)
# Enregistrement du modèle Category avec la classe d'administration CategoryAdmin
admin.site.register(Post, PostAdmin)
# Enregistrement du modèle Post avec la classe d'administration PostAdmin
admin.site.register(Comment, CommentAdmin)
# Enregistrement du modèle Comment avec la classe d'administration CommentAdmin