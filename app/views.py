from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView , View
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserProfileForm
from .models import Category, Pastry,Recipe, BakingTip, Comment, UserProfile, Rating
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'app/Home.html'

class ContactPageView(TemplateView):
    template_name = 'app/Contact.html'

class AboutPageView(TemplateView):
    template_name = 'app/About.html'


class UserLoginView(LoginView):
    template_name = 'app/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserRegisterView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
        return render(request, 'app/register.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user
            user = user_form.save()

            # Save the profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect(reverse_lazy('login'))

        return render(request, 'app/register.html', {'user_form': user_form, 'profile_form': profile_form})

# Category List View
class CategoryListView(ListView):
    model = Category
    template_name = 'app/category_list.html'
    context_object_name = 'categories'



class PastryListView(ListView):
    model = Pastry
    template_name = 'app/pastry_list.html'
    context_object_name = 'pastries'

class PastryDetailView(DetailView):
    model = Pastry
    template_name = 'app/pastry_detail.html'
    context_object_name = 'pastry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = Rating.objects.filter(pastry=self.object)
        context['average_rating'] = (
            sum(rating.score for rating in context['ratings']) / context['ratings'].count()
            if context['ratings'].exists()
            else None
        )
        context['comments'] = Comment.objects.filter(pastry=self.object)
        return context


class PastryUpdateView(UpdateView):
    model = Pastry
    fields = '__all__'
    context_object_name = 'pastry'
    template_name = 'app/update_pastry.html'

class PastryDeleteView(DeleteView):
    model = Pastry
    template_name = 'app/delete_pastry.html'
    success_url = reverse_lazy('pastries')






class RecipeListView(ListView):
    model = Recipe
    template_name = 'app/recipe_list.html'
    context_object_name = 'recipes'

class PastryCreateView(CreateView):
    model = Pastry
    template_name = 'app/create_pastry.html'
    fields = '__all__'
    success_url = reverse_lazy('pastries')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

# Recipe Detail View
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'app/recipe_detail.html'
    context_object_name = 'recipe'

# Recipe Create View (Optional: Only for Admin or Pastry Creators)
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'app/add_recipe.html'
    fields = ['pastry', 'ingredients', 'procedure']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pastries'] = Pastry.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('pastries')

# Recipe Update View
class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'app/update_recipe.html'
    fields = ['ingredients', 'procedure']

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})






class BakingTipListView(ListView):
    model = BakingTip
    template_name = 'app/baking_tips.html'
    context_object_name = 'tips'


class BakingTipDetailView(DetailView):
    model = BakingTip
    template_name = 'app/baking_tip_detail.html'
    context_object_name = 'tip'


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'app/user_profile.html'
    context_object_name = 'users'

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'app/add_comment.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.pastry = get_object_or_404(Pastry, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pastry_detail', kwargs={'pk': self.kwargs['pk']})


class RatingCreateView(LoginRequiredMixin, CreateView):
    model = Rating
    template_name = 'app/add_rating.html'
    fields = ['score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.pastry = get_object_or_404(Pastry, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pastry_detail', kwargs={'pk': self.kwargs['pk']})