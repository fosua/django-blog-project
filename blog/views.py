# Create your views here.
from django.template import Context, loader, Template
from django.http import HttpResponse


from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    each_post = ''
    for item in post_list:
        each_post += str(item) + ' '
    return HttpResponse(each_post)

def post_detail(request, ID, showComments=False):
    
    posts = Post.objects.get(id = ID)
    comments = ''
    if showComments != None:
        for c in posts.comment_set.all():
            comments += str(c) +' ' 
    #return HttpResponse(posts)
    Html = "<html><body> post_title: %s</br> comments: %s </body></html> "% (posts , comments)
    #output = str(posts) + ' ' + comments
    return HttpResponse( Html)
    
    
    
def post_search(request, anything):
    result = Post.objects.filter(body__icontains = anything)
    title_body = ''
    #for i in result:
        #title_body += i.title + ' : ' +i.body + ', '
    html = Template("<html><body>{% for i in results %}<p>{{i.title}}: {{i.body}}:</p>{% endfor %} </body></html>")
    c = Context ({'results':result})
      
    #return HttpResponse(title_body)
    return HttpResponse( html.render(c))

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
