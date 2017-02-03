from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from teleconsultoria.views import LoginView, LogoutView, PainelAdminView
from teleconsultoria.views import GerenciarTeleconsultorView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login_view"),
    url(r'^logout', LogoutView.as_view(), name="logout_view"),
    url(r'^painel/administracao$', 
        login_required(PainelAdminView.as_view()), name="painel_view"),
    url(r'^painel/gerenciar-teleconsultor$',
        login_required(GerenciarTeleconsultorView.as_view()),
        name="gerenciar_teleconsultor_view"),
    url(r'^admin/', include(admin.site.urls)),
]
