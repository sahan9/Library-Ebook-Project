from django.shortcuts import render,get_object_or_404,redirect
from bookapp.models import Post, Comment
from bookapp.forms import PostForm, CommentForm
from django.utils import timezone

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from django.views.generic import (TemplateView, 
                                  ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


# PDF reader
class HelloPDFView(PDFTemplateView):
    template_name = 'list.html'


class PdfDetail(PDFTemplateResponseMixin,DetailView):
    model = Post
    template_name = 'pdf_detial.html'
# PDF reader



class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'bookapp/post_detail.html'
    form_class = PostForm
    model = Post



class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'bookapp/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'bookapp/post_list.html'
    model = Post


    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')





def chart_data(request):

    data_list = Post.objects.all()

    data_dict = {'Data_record':data_list}

    return render(request, 'chart.html', context= data_dict)
        



#########################################################################################


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)




def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()
    return render(request, 'bookapp/comment_form.html',{'form':form})



@login_required
def comment_approval(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)