from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)
from django.shortcuts import get_object_or_404
from .models import Category, Comment, Post

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.order_by('-data_postagem')
        return context


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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['autor', 'texto']
        labels = {'autor': 'Autor', 'texto': 'Comentário'}


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comentario.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def form_valid(self, form):
        form.instance.post = self.post_obj
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detalhe', kwargs={'pk': self.post_obj.pk})

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/categorias.html'
    context_object_name = 'categorias'
    ordering = ['nome']


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/lista.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.order_by('-data_postagem')
        return context