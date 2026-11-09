from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']


def lista(request):
    posts = Post.objects.order_by('-data_postagem')
    return render(request, 'blog/lista.html', {'posts': posts})


def detalhe(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhe.html', {'post': post})


def criar(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return redirect('detalhe', pk=post.pk)
    return render(request, 'blog/form.html', {'form': form, 'acao': 'Novo post'})


def editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detalhe', pk=pk)
    return render(request, 'blog/form.html', {'form': form, 'acao': 'Editar post'})


def remover(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista')
    return render(request, 'blog/confirmar_remocao.html', {'post': post})