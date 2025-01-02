from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    CategoryListView,
                    PastryListView,
                    PastryCreateView,
                    PastryDetailView,
                    PastryDeleteView,
                    BakingTipListView,
                    BakingTipDetailView,
                    UserProfileDetailView,
                    CommentCreateView,
                    RatingCreateView,
                    UserLoginView,
                    UserLogoutView,
                    UserRegisterView,
                    RecipeListView,
                    RecipeDetailView,
                    RecipeCreateView,
                    RecipeUpdateView, PastryUpdateView)

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),  # Home page
    path('contact/', ContactPageView.as_view(), name='contact'),  # Contact page
    path('about/', AboutPageView.as_view(), name='about'),  # About page
    path('category_list/', CategoryListView.as_view(), name='category_list'),  # Category list page
    path('', PastryListView.as_view(), name='pastries'),  # Pastries list page
    path('pasties/add/', PastryCreateView.as_view(), name='create_pastry'),
    path('pastries/<int:pk>/', PastryDetailView.as_view(), name='pastry_detail'),  # Pastry detail page
    path('pastries/<int:pk>/update/', PastryUpdateView.as_view(), name='update_pastry'),
    path('pastries/<int:pk>/delete/', PastryDeleteView.as_view(), name='delete_pastry'),
    path('baking-tips/', BakingTipListView.as_view(), name='baking_tips'),  # Baking tips list page
    path('baking-tips/<int:pk>/', BakingTipDetailView.as_view(), name='baking_tip_detail'),  # Baking tip detail page
    path('profile/', UserProfileDetailView.as_view(), name='user_profile'),  # User profile page
    path('pastries/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),  # Add comment to pastry
    path('pastries/<int:pk>/rating/', RatingCreateView.as_view(), name='add_rating'),  # Add rating to pastry
    path('login/', UserLoginView.as_view(), name='login'),  # Login page
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Logout page
    path('register/', UserRegisterView.as_view(), name='register'),  # Registration page

    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/add/', RecipeCreateView.as_view(), name='add_recipe'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='update_recipe'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)