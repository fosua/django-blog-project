# Create your views here.
from django.template import Context, loader, Template
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    #each_post = ''
    t = loader.get_template('blog/post_list.html')
    c = Context({ 'post_list': post_list})
    """for item in post_list:
        each_post += str(item) + ' '"""
    return HttpResponse(t.render(c))

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['post_comment']
@csrf_exempt
def post_detail(request, ID, showComments=False):
    posts = Post.objects.get(id = ID)
    comments = posts.comment_set.all()
    if request.method == 'POST':
        comment = Comment(post = posts)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    #t = loader.get_template('blog/post_detail.html')
    #C = Context({'post_detail': posts, 'comment':comments})
    """if showComments != None:
        for c in posts.comment_set.all():
            comments += str(c) +' ' 
    #return HttpResponse(posts)
    Html = "<html><body> post_title: %s</br> comments: %s </body></html> "% (posts , comments)
    #output = str(posts) + ' ' + comments"""
    #return HttpResponse(t.render(C))
    return render_to_response('blog/post_detail.html', {'post_detail': posts, 'comment':comments, 'form':form})
@csrf_exempt
def edit_comment(request, comm_id):
    comments = Comment.objects.get(id = comm_id)
    posts = comments.post_comment
    if request.method == 'POST':
        
        form = CommentForm(request.POST, instance = comments)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(posts.get_absolute_url())
    else:
        form = CommentForm(instance = comments)
        return render_to_response('blog/edit_comment.html', { 'edit_comment': comments, 'comm_post':posts, 'form':form})
def post_search(request, anything):
    result = Post.objects.filter(body__icontains = anything)
    #title_body = ''
    #for i in result:
    #title_body += i.title + ' : ' +i.body + ', '
    """html = Template("<html><body>{% for i in results %}<p>{{i.title}}: {{i.body}}:</p>{% endfor %} </body></html>")
#return HttpResponse(title_body)"""
    
    #t = loader.get_template('blog/post_search.html')
    #c = Context ({'results':result}) 
    
    #return HttpResponse( t.render(c))
    return render_to_response('blog/post_search.html', {'results':result})

def home(request):
    """print 'it works'
    return HttpResponse('hello world. Ete zene?') """
    return render_to_response('blog/base.html', {})
