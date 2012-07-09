# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(str(post_list))

def post_detail(request, id, showComments=False):
    """posts = Post.objects.all(id)
    comments = Comment.object.all(id)
    if showComments == False:
        
        return HttpResponse(posts)
    else:
        return (HttpResponse(id, )"""
    
    
    
def post_search(request, term):
    result = str(term)
    return HttpResponse(result)

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
