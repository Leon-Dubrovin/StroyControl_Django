from django.urls import path,re_path
from stroycontrol import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.main_page),
    path("about/", views.about),
    path("SK/", views.SK),
    path("TKzaII/", views.TKzaII),
    path("DK/", views.DK),
    path("techzakaz/", views.techzakaz),
    path("TA/", views.TA),
    path("contacts/", views.contacts),
    path("reg_predp/<int:id>", views.reg_predp),
    path("reg/", views.reg),
    path("reg/user_create/", views.create_user),
    path("filter_zakazchik/<int:id>",views.filter_zakazchik),
    path("filter_podryadchik/<int:id>",views.filter_podryadchik),
    path("filter_predp_date/<int:id>",views.filter_predp_date),
    path("kab/<int:id>", views.kab),
    path("prov/", views.prov)
]
