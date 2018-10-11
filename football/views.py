from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, get_object_or_404
from .models import Country, NewsPage, Comment, UserProfile
from django.views.generic import TemplateView, DetailView, UpdateView
from football.forms import RegistrationForm, CommentForm, ProfileForm
from django.contrib.auth import login, authenticate
from rest_framework import generics
from .serializers import CommentSerializer

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        news = NewsPage.objects.all()
        users = UserProfile.objects.all()
        return {'countries': countries, 'news': news, 'users': users}


def show_country(request, slug):
    context_dict = {}
    countries = Country.objects.all()
    context_dict['countries'] = countries
    country = Country.objects.filter(slug=slug)
    if country:
        country = country[0]
        news = NewsPage.objects.filter(country=country)
        context_dict['news'] = news
        context_dict['country'] = country
    else:
        context_dict['news'] = None
        context_dict['country'] = None

    return render(request, 'country_news.html', context_dict)


#class ShowCountry(DetailView):
#    template_name = 'country_news.html'

#    def get_context_data(self, **kwargs):
#        countries = Country.objects.
    
#    def get_context_data(self, **kwargs):
#        news = NewsPage.objects.all()
#        countries = Country.objects.all()
#        return {'news_list': news, 'country': countries}

class ShowNewsPage(DetailView):
    template_name = 'news_page.html'
    model = NewsPage

    def get_context_data(self, **kwargs):
        context = super(ShowNewsPage, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news_page=context['object'])
        context['countries'] = Country.objects.all()
        parent_comments = []
        sub_comments = []
        sorted_comments = []
        context['sorted_comments'] = {}

        for i in context['comments']:
            if i.father_comment is None:
                parent_comments.append(i)
            else:
                sub_comments.append(i)

        for par_comment in parent_comments:
            low_comments = []
            for sub_comment in sub_comments:
                if sub_comment.father_comment == par_comment:
                    low_comments.append(sub_comment)
            sorted_comments1 = dict([(par_comment, low_comments)])
            sorted_comments.append(sorted_comments1)

        for i in sorted_comments:
            for j in i.items():
                    context['sorted_comments'][j[0]] = j[1]

        context['form'] = CommentForm()

        total_comments = 0
        for i in list(context['comments']):
            total_comments = total_comments + 1
        context['total_comments'] = total_comments
        print(total_comments)

        return context

    def post(self,request, *args, **kwargs):
        comment = Comment()
        comment.comment_text = request.POST.get('comment')
        comment.news_page = self.get_object()
        comment.user = UserProfile.objects.get(user__username=request.user.username)
        if comment.comment_text:
            comment.save()
        return HttpResponseRedirect(reverse("football:news_page", kwargs=self.kwargs))


def add_second_comment(request, slug, com_pk):
    data = request.POST.copy()
    print(request.POST)
    usr = UserProfile.objects.get(username=request.user.username)
    if request.user.is_authenticated():
        q = Comment(user=usr)
    q.comment_text = data['comment']
    q.news_page = NewsPage.objects.get(slug=slug)
    q.user = usr
    q.father_comment = Comment.objects.get(pk=com_pk)
    q.save()

    return redirect('football:news_page', slug)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            a = UserProfile(user=user)
            a.save()
            return redirect('homepage')

    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


class Account(UpdateView):
    template_name = 'registration/account.html'
    model = UserProfile
    success_url = '/'
    form_class = ProfileForm

    def post(self, request, *args, **kwargs):
        print(request.POST)
        a = super(Account, self).post(request, *args, **kwargs)
        return a
        return super(Account, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        a = super(Account, self).get(request, *args, **kwargs)
        return a
        return super(Account, self).post(request, *args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        queryset = queryset.filter(user__username=self.request.user.username)
        print(queryset)
        obj = get_object_or_404(queryset)

        return obj


def search(request):
    context_dict = {}
    context_dict['countries'] = Country.objects.all()
    query = request.GET.get('q')
    context_dict['results'] = NewsPage.objects.filter(text__search=query)
    context_dict['query'] = query
    return render(request, 'search_results.html', context_dict)

# define api views

