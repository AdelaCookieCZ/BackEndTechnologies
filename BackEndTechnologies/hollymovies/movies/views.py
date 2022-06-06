from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from movies.models import Movie, Actor, Director, Contact, Profile
from books.models import BaseBook
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from movies.forms import ContactForm, MovieForm, ActorForm, DirectorForm, ProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin




class HomepageView(View):
    def get(self, request, *args, **kwargs):
        context = {
                'number_of_movies': Movie.objects.all().count(),
                'number_of_actors': Actor.objects.all().count(),
                'number_of_directors': Director.objects.all().count(),
                'number_of_books': BaseBook.objects.all().count(),
                'page_name': 'Homepage',
            }
        return TemplateResponse(request, 'homepage.html', context=context)


# def homepage_view(request):
#     context = {
#         'number_of_movies': Movie.objects.all().count(),
#         'number_of_actors': Actor.objects.all().count(),
#         'page_name': 'Homepage',
#     }
#     return TemplateResponse(request, 'homepage.html', context=context) #mame URLs, ktere nam definuje, kam to odkaze uzivatele

class ActorListView(LoginRequiredMixin, ListView):
    model = Actor
    template_name = 'actors.html'
    extra_context = {'page_name': 'Actors'}


# def actors_view(request):
#     actors = Actor.objects.all()
#     context = {
#         'all_actors': actors,
#         'page_name': 'Actors',
#     }
#     return TemplateResponse(request, 'actors.html', context=context)


class MoviesListView(LoginRequiredMixin, ListView):
    queryset = Movie.objects.all().order_by('-rating')
    template_name = 'movies.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MoviesListView, self).get_context_data(*args, **kwargs)
        context.update({
            'best_movies': Movie.objects.filter(rating__gte=80).order_by('-rating'),
            'worst_movies': Movie.objects.filter(rating__lte=20).order_by('rating'),
            'page_name': 'Movies',
        })
        return context


class HollyMoviesDetailView(LoginRequiredMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(HollyMoviesDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class DirectorListView(LoginRequiredMixin, ListView):
    model = Director
    template_name = 'directors.html'
    extra_context = {'page_name': 'Directors'}


class DirectorDetailView(HollyMoviesDetailView):
    model = Director
    template_name = 'director_detail.html'    #mohlo by byt i actor detail, ktery je uplne stejny a nemusi se vytvaret


class MovieDetailView(UserPassesTestMixin, HollyMoviesDetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def post(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        movie.likes += 1
        movie.save(update_fields=['likes', ]) #rikame, ze jsme zmenili jen liky, vse ostatni zustane tak, jak je (rychlejsi)
        return redirect('movie_detail', pk=pk) #redirect = po post requestu se dostaneme zpatky na get a uvidime zmenu automaticky na strance

    def test_func(self):
        if self.request.user.username == 'honza':       #pro Honzu bude zakazna nahlizet na detail filmu
            return False
        return True


class ActorDetailView(HollyMoviesDetailView):
    model = Actor
    template_name = 'actor_detail.html'



# def movies_view(request):
#     all_movies = Movie.objects.all().order_by('-rating') #budese radit od nejvetsiho po nejmensi
#     best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')
#     worst_movies = Movie.objects.filter(rating__lte=30).order_by('rating') #definice filtru, ktere chceme zobrazit na strance
#     context = {
#             'all_movies': all_movies,
#             'best_movies': best_movies,
#             'worst_movies': worst_movies,
#             'page_name': 'Movies',
#         }
#     return TemplateResponse(request, 'movies.html', context=context)

def jinja2_testing_view(request):
    index_list = ['index1', 'index2', 'index3']
    index_1 = index_list[0]

    testing_dict = {'key_1': 'value1', 'key_2': 'value2'}
    value_1 = testing_dict['key_1']
    context = {
        'testing_list': ['index1', 'index2', 'index3'],
        'testing_dict': {'key_1': 'value1', 'key_2': 'value2'},
        'testing_queryset': Movie.objects.all(),
    }
    return TemplateResponse(request, 'jinja2_testing.html', context=context)

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'contact_form': ContactForm()
#         }
#         return TemplateResponse(request, 'contact.html', context=context)
#
#     def post(self, request, *args, **kwargs):
#         bounded_form = ContactForm(request.POST) #vazana forma s daty
#         if not bounded_form.is_valid():
#             return TemplateResponse(request, 'contact.html', context={'contact_form': bounded_form})
#         name = bounded_form.cleaned_data.get('name')
#         phone_number = bounded_form.cleaned_data.get('phone_number')
#         email = bounded_form.cleaned_data.get('email')
#         subject = bounded_form.cleaned_data.get('subject')
#         contact_at = bounded_form.cleaned_data.get('contact_at')
#
#         Contact.objects.create(
#             name=name,
#             phone_number=phone_number,
#             email=email,
#             subject=subject,
#             contact_at=contact_at
#         )
#         return TemplateResponse(request, 'contact.html', context={'contact_form': ContactForm()})


class ContactView(LoginRequiredMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        contact_at = form.cleaned_data.get('contact_at')

        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            contact_at=contact_at
        )
        return TemplateResponse(self.request, 'contact.html', context={'form': ContactForm()})

    def form_invalid(self, form):
        return TemplateResponse(self.request,'contact.html', context={'form': form})


class CreateMovieView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    template_name = 'movie_create.html'
    form_class = MovieForm
    model = Movie
    permission_required = 'movies.add_movie'


class CreateActorView(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'actor_create.html'
    form_class = ActorForm
    model = Actor
    permission_required = 'movies.add_actor'


class UpdateMovieView(LoginRequiredMixin,UpdateView):
    template_name = 'movie_update.html'
    form_class = MovieForm
    model = Movie


class UpdateActorView(LoginRequiredMixin,UpdateView):
    template_name = 'actor_update.html'
    form_class = ActorForm
    model = Actor


class DeleteMovieView(LoginRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('all_movies')


class DeleteActorView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'actor_confirm_delete.html'
    model = Actor
    success_url = reverse_lazy('all_actors')
    permission_required = 'movies.delete_actor'


class CreateDirectorView(PermissionRequiredMixin, LoginRequiredMixin,CreateView):
    template_name = 'director_create.html'
    form_class = DirectorForm
    model = Director
    permission_required = 'movies.add_director'


class UpdateDirectorView(LoginRequiredMixin, UpdateView):
    template_name = 'director_update.html'
    form_class = DirectorForm
    model = Director


class DeleteDirectorView(LoginRequiredMixin, DeleteView):
    template_name = 'director_confirm_delete.html'
    model = Director
    success_url = reverse_lazy('all_directors')


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileCreateView(CreateView):
    form_class = ProfileForm
    template_name = 'registration/profile_create.html'
    success_url = reverse_lazy('homepage')

    def get_form_kwargs(self):
        kwargs = super(ProfileCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class ProfileUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile_update.html'
    success_url = reverse_lazy('homepage')
    model = Profile

    def get_form_kwargs(self):
        kwargs = super(ProfileUpdateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def test_func(self):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        return profile.user == self.request.user