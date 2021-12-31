from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from blog.forms import PostForm
from blog.models import Post


#블로그 메인페이지
def index(request):
    #models에서 자료 가져오기
    post_list = Post.objects.all()
    #자료 보내주기
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)

def test(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/post_detail.html', context)

#글목록
def post_list(request):
    pass

def detail(request):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'post/post_detail.html', context)

#글쓰기 등록
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)        #폼에 입력된 자료 가져오기
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:index')       #등록 후 블로그홈으로 경로 이동
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)



