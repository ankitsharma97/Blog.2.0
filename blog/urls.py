from django.urls import path
from blog import views
from mainblog import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index ,name='home'),
    path('about', views.about ,name='about'),
    path('contact', views.contact ,name='contact'),
    path('login', views.login ,name='login'),
    path('signup', views.signup ,name='signup'),
    path('logout', views.logout ,name='logout'),
    path('dashboard', views.dashboard ,name='dashboard'),
    path('add_post', views.add_post ,name='add_post'),
    path('update_post/<int:id>', views.update_post ,name='update_post'),
    path('delete_post/<int:id>', views.delete_post ,name='delete_post'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)