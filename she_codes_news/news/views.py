from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/login/'
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class DeleteStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    login_url = 'users/login/'
    model = NewsStory
    template_name = 'news/delete-story.html'
    success_url = reverse_lazy('news:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = 'users/login/'
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/update-story.html'

    def get_success_url(self):
        pk = self.kwargs('pk')
        success_url = reverse_lazy('news:story', kwargs={pk: pk})
        return success_url

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
