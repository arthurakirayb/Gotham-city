from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()  # armazenado como HTML
    data_postagem = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(
        Category, related_name='posts', blank=True
    )

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comentarios'
    )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.autor} em {self.post}'