from django.urls import path, include


from . import views

app_name = 'team_fundraising'

urlpatterns = [
    path('', views.index_view, name='index'),
    path(
        'fundraiser/<int:fundraiser_id>/',
        views.fundraiser_view,
        name='fundraiser'
    ),
    path(
        'donation/<int:fundraiser_id>/', views.new_donation, name="donation"),
    path(
        'accounts/update_fundraiser/',
        views.update_fundraiser,
        name="update_fundraiser",
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name="signup"),
]
