from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from main.models import VehicleInstance
from main.forms import AddPostForm


def index(request):
    template = 'main/index.html'
    ip = request.META.get('REMOTE_ADDR')  # just 4 test
    browser = request.META.get('HTTP_USER_AGENT')  # just 4 test
    posts = VehicleInstance.objects.filter(is_active=True)
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts, 'page': page, 'ip': ip, 'browser': browser}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(VehicleInstance, id=id, is_active=True)
    template = 'main/post-detail.html'
    return render_to_response(template, {'post': post, })


# @login_required
# def AddPost(request, item_id):
#     item = get_object_or_404(VehicleInstance, id=item_id)
#     form = forms.ItemDescForm(request.POST or None, instance=item)
#     context = { 'item': item, 'form': form, }
#     if request.method == 'POST' and form.is_valid():
#         form.save(request.user)
#         return redirect('item_desc', item_id=item.id)
#     return direct_to_template(request, 'form.html', context)


class AddPost(View):
    def get(self, request):
        form = AddPostForm
        return render(request, 'registration/add_post.html', context={'form': form})

    def post(self, request):
        bound_form = AddPostForm(request.POST)

        if bound_form.is_valid():
            # new_review = bound_form.save()
            return redirect('main:index')
        return render(request, 'registration/add_post.html', context={'form': bound_form})

# def search(request):
#     errors = []
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             errors.append('Введіть пошуковий запит')
#         elif len(q) > 20:
#             errors.append('Введіть не більше 20 символів')
#         else:
#             posts = TestVehicle.objects.filter(title__icontains=q)
#             return render_to_response('main/search-results.html',
#                                       {'posts': posts, 'query': q})
#     return render_to_response('main/search.html', {'errors': errors})
