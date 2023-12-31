# views.py
from django.shortcuts import render
from django.http import HttpResponse
from post.models import Message

def index(request):
    latest = Message.objects.order_by('-created')[:7]
    context = {'latest': latest}
    return render(request, 'post/index.html', context)

def write(request):
    if request.method == "POST":
        return render(request, 'post/write.html', {})
    
    req = request.POST
    writer = req['writer'] # �ۼ���
    receiver = req['receiver'] # ������
    content = req['content'] # ����
    writing_pad = req['writing_pad'] #������
    # emoticon = req['emoticon']
    # created_at = req['created_at']
    disclosure = req['disclosure']
    #opened �� �ۼ��ÿ� �ʿ� ���� �� ���Ƽ� �ϴ� �����
    message_dict = {'writer': writer, 'content': content, 'writing_pad' : writing_pad, 'disclosure' : disclosure,}

    # Error handling
    if len(writer) == 0:
        message_dict['error'] = "please enter writer"
    if len(receiver) == 0:
        message_dict['error'] = "please enter receiver"
    elif len(content) == 0:
        message_dict['error'] = "please enter contet"
    elif len(content) > 1500:
        message_dict['error'] = "content is too long"
    elif len(writing_pad) == 0:
        message_dict['error'] = "please enter writing pad"

    if 'error' in message_dict:
        return render(request, 'post/write.html', message_dict)
    else:
        msg = Message.create(writer, content)
        msg.save()
        return HttpResponse("�ۼ� �Ŀ��� ����/������ �Ұ����մϴ�.")
    
def list(request): #������� �ҷ�����
    if request.method == "GET":
        return render(request, 'post/list.html', {})
    
    req = request.GET
    writer = req['writer'] # �ۼ���
    disclosure = req['disclosure'] # ��������
    receiver = req['receiver'] # ������
    content = req['content'] # ����
    writing_pad = req['writing_pad'] #������
    message_dict = {'writer': writer, 'content': content, 'writing_pad' : writing_pad, 'disclosure' : disclosure, 'receiver' : receiver}

    # Error handling

    if 'error' in message_dict: #���� �߻��� ���� �������� ���ư�
        return render(request, 'main.html', message_dict) 
    else: #�����۵�
        return render(request, 'post/list.html', {})

def list(request): #������� �ҷ�����
    if request.method == "GET":
        return render(request, 'post/list.html', {})
    
    req = request.GET
    writer = req['writer'] # �ۼ���
    disclosure = req['disclosure'] # ��������
    receiver = req['receiver'] # ������
    content = req['content'] # ����
    writing_pad = req['writing_pad'] #������
    message_dict = {'writer': writer, 'content': content, 'writing_pad' : writing_pad, 'disclosure' : disclosure, 'receiver' : receiver}

    # Error handling

    if 'error' in message_dict: #���� �߻��� ���� �������� ���ư�
        return render(request, 'main.html', message_dict) 
    else: #�����۵�
        return render(request, 'post/list.html', {})

def letter(request): #���� Ȯ���ϱ�
    messages = Message.objects.all()

    # �ʿ��� �ʵ���� �����Ͽ� ����Ʈ�� ����
    message_data = []
    for message in messages:
        message_data.append({
            'writer': messages.writer,
            'content': messages.content,
            'writing_pad': messages.writing_pad,
            'emoticon': messages.emoticon,
            'created_at': messages.created_at,
            'disclosure': messages.disclosure,
            'name': messages.name,
        })

    return HttpResponse({'posts': message_data})