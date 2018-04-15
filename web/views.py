from django.http import HttpResponse 
from web.models import Message 
from django.template import RequestContext 
from web.forms import MessageForm 
from django.utils import timezone 
from django.shortcuts import render_to_response, redirect

def board(request):
		messages = Message.objects.all() 
		response_string = "<a href='/post'>Post</a><hr/>" 
		response_string += '<br/>'.join(["%s : %s" % (q.title , q.subject) for q in messages]) 
		return HttpResponse(response_string) 
def post(request): 
    if request.method == 'POST': 
        form = MessageForm(request.POST) 
        if form.is_valid(): 
            message = Message(title=form.cleaned_data['title'],subject=form.cleaned_data['subject']) 
            message.save() 
            return redirect('/board') 
    else: 
        form = MessageForm() 
    return render_to_response('post.html',{'form': form}, context_instance=RequestContext(request)) 
