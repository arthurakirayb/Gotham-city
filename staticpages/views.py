from django.shortcuts import get_object_or_404, redirect, render

from .models import Post


def lista(request):
    posts = Post.objects.order_by('-data_postagem')
    return render(request, 'blog/lista.html', {'posts': posts})


def detalhe(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalhe.html', {'post': post})


def criar(request):
    if request.method == 'POST':
        post = Post(
            titulo=request.POST['titulo'],
            conteudo=request.POST['conteudo'],
        )
        post.save()
        return redirect('detalhe', pk=post.pk)
    return render(request, 'blog/form.html', {'acao': 'Novo post'})


def editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.titulo = request.POST['titulo']
        post.conteudo = request.POST['conteudo']
        post.save()
        return redirect('detalhe', pk=post.pk)
    return render(request, 'blog/form.html', {'acao': 'Editar post', 'post': post})


def remover(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista')
    return render(request, 'blog/confirmar_remocao.html', {'post': post})