from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        labels = {'titulo': 'Título', 'conteudo': 'Conteúdo (HTML)'}


class PostListView(ListView):
    model = Post
    template_name = 'blog/lista.html'
    context_object_name = 'posts'
    ordering = ['-data_postagem']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalhe.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    extra_context = {'acao': 'Novo post'}

    def get_success_url(self):
        return reverse('detalhe', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    extra_context = {'acao': 'Editar post'}

    def get_success_url(self):
        return reverse('detalhe', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/confirmar_remocao.html'
    context_object_name = 'post'
    success_url = reverse_lazy('lista')