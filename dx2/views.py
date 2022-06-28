from django.shortcuts import render, redirect

# Create your views here.
from dx2.form import PostForm
from dx2.models import board, PostImage

"""
def createboard(request):
    if request.method == 'GET':
        modelform = PostForm()
        return render(request,'board/board.html',{'modelform':modelform})
    elif request.method == 'POST':
        modelform = PostForm(request.POST)
        if modelform.is_valid():
            post = modelform.save(commit = False)
            post.image = request.FILES.get('image',None) #request의 FILES의 image 속성 가져온다
            post.save()
            return redirect('/post/onelist/'+ str(post.id))"""

def createboard(request):
    if request.method == 'GET':
        modelform = PostForm()
        return render(request,'board/board.html',{'modelform':modelform})
    elif request.method == 'POST':
        modelform = PostForm(request.POST)
        if modelform.is_valid():
            post = modelform.save(commit = False)
            post.save() #게시글 저장
            for image in request.FILES.getlist('image',None):
                postImage = PostImage()
                postImage.image = image
                postImage.post = post
                postImage.save()
            return redirect('/post/onelist/'+ str(post.id))



def readboard(request):
    model = board.objects.all()
    return render(request, 'board/boardlist.html',{'datas':model})

def readoneboard(request, bid):
    """
    post = board.objects.get(id=bid)
    model = PostImage.objects.filter(post_id=post.id)
    return render(request, 'board/boardonelist.html', {'imgs': model, 'post': post}) """

    post = board.objects.prefetch_related('postimage_set').get(id=bid)
    return render(request, 'board/boardonelist.html', {'post': post})