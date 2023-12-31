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
    writer = req['writer'] # 작성자
    receiver = req['receiver'] # 수신자
    content = req['content'] # 내용
    writing_pad = req['writing_pad'] #편지지
    # emoticon = req['emoticon']
    # created_at = req['created_at']
    disclosure = req['disclosure']
    #opened 는 작성시에 필요 없는 것 같아서 일단 뺐어요
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
        return HttpResponse("작성 후에는 수정/삭제가 불가능합니다.")
    
def list(request): #편지목록 불러오기
    if request.method == "GET":
        return render(request, 'post/list.html', {})
    
    req = request.GET
    writer = req['writer'] # 작성자
    disclosure = req['disclosure'] # 열람여부
    receiver = req['receiver'] # 수신자
    content = req['content'] # 내용
    writing_pad = req['writing_pad'] #편지지
    message_dict = {'writer': writer, 'content': content, 'writing_pad' : writing_pad, 'disclosure' : disclosure, 'receiver' : receiver}

    # Error handling

    if 'error' in message_dict: #에러 발생시 이전 페이지로 돌아감
        return render(request, 'main.html', message_dict) 
    else: #정상작동
        return render(request, 'post/list.html', {})

def list(request): #편지목록 불러오기
    if request.method == "GET":
        return render(request, 'post/list.html', {})
    
    req = request.GET
    writer = req['writer'] # 작성자
    disclosure = req['disclosure'] # 열람여부
    receiver = req['receiver'] # 수신자
    content = req['content'] # 내용
    writing_pad = req['writing_pad'] #편지지
    message_dict = {'writer': writer, 'content': content, 'writing_pad' : writing_pad, 'disclosure' : disclosure, 'receiver' : receiver}

    # Error handling

    if 'error' in message_dict: #에러 발생시 이전 페이지로 돌아감
        return render(request, 'main.html', message_dict) 
    else: #정상작동
        return render(request, 'post/list.html', {})

def letter(request): #편지 확인하기
    messages = Message.objects.all()

    # 필요한 필드들을 추출하여 리스트에 저장
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