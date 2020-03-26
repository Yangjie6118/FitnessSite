from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Commentary
from django.urls import reverse
from django.http import JsonResponse
from .forms import CommentaryForm


def update_comment(request):
    """
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message1': '用户未登录'})

    text = request.POST.get('teJsonResponsext', '').strip()
    if text == '':
        return render(request, 'error.html', {'message1': '评论内容为空'})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'message1': '评论对象不存在', 'redirect_to': referer})

    comment = Commentary()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    referer = request.META.get('HTTP_REFERER', reverse('base'))
    return redirect(referer)
    """
    comment_form = CommentaryForm(request.POST, user=request.user)
    data = {}
    if comment_form.is_valid():
        # 检查通过保存数据
        comment = Commentary()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        # 发送邮件通知
        comment.send_mail()

        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        #  ajax返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.get_nickname_or_username()
        data['created_time'] = comment.created_time.timestamp()
        data['text'] = comment.text
        data['content_type'] = ContentType.objects.get_for_model(comment).model
        if not parent is None:
            data['reply_to'] = comment.reply_to.get_nickname_or_username()
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if not comment.root is None else ''
    else:
        # return render(request, 'error.html', {'message1': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)
