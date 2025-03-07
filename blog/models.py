from django.db import models
# Importation du module models de Django pour créer des modèles de base de données

# Vous allez avoir besoin de trois modèles distincts pour le blog :
# Post
# Category
# Comment

class Category(models.Model):
    # Modèle pour les catégories de blog
    name = models.CharField(max_length=30)
    # Champ de caractère pour le nom de la catégorie, avec une longueur maximale de 30 caractères

    class Meta:
        verbose_name_plural = "categories"
        # Définit le nom pluriel de la catégorie pour l'affichage dans l'interface d'administration

    def __str__(self):
        return self.name
        # Méthode pour retourner une représentation en chaîne de caractères de l'objet Category

class Post(models.Model):
    # Modèle pour les posts de blog
    title = models.CharField(max_length=255)
    # Champ de caractère pour le titre du post, avec une longueur maximale de 255 caractères
    body = models.TextField()
    # Champ de texte pour le contenu du post
    created_on = models.DateTimeField(auto_now_add=True)
    # Champ de date et heure pour la date de création du post, défini automatiquement à la création
    last_modified = models.DateTimeField(auto_now=True)
    # Champ de date et heure pour la dernière modification du post, mis à jour automatiquement à chaque modification
    categories = models.ManyToManyField("Category", related_name="posts")
    # Champ de relation ManyToMany avec le modèle Category, avec un nom de relation inversée "posts"
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.title
        # Méthode pour retourner une représentation en chaîne de caractères de l'objet Post

class Comment(models.Model):
    # Modèle pour les commentaires sur les posts de blog
    author = models.CharField(max_length=60)
    # Champ de caractère pour le nom de l'auteur du commentaire, avec une longueur maximale de 60 caractères
    body = models.TextField()
    # Champ de texte pour le contenu du commentaire
    created_on = models.DateTimeField(auto_now_add=True)
    # Champ de date et heure pour la date de création du commentaire, défini automatiquement à la création
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    # Champ de relation ForeignKey avec le modèle Post, avec suppression en cascade des commentaires si le post est supprimé

    def __str__(self):
        return f"{self.author} on '{self.post}'"
        # Méthode pour retourner une représentation en chaîne de caractères de l'objet Comment