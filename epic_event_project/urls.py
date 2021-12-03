"""epic_event_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.conf import settings
from rest_framework import routers
#from rest_framework_nested import routers
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from client.views import ClientViewset
from contract.views import ContractViewset
from event.views import EventViewset
#from client.views import RegisterApi

# création du routeur
router = routers.SimpleRouter()
# déclaration de project afin de générer l'URL correspondante
client_router = routers.SimpleRouter(trailing_slash=False)
client_router.register(r"client/?", ClientViewset, basename="client")

contract_router = routers.SimpleRouter(trailing_slash=False)
contract_router.register(r"contract/?", ContractViewset, basename="contract")

event_router = routers.SimpleRouter(trailing_slash=False)
event_router.register(r"event/?", EventViewset, basename="event")


urlpatterns = [
    path('', include(client_router.urls)),
    path('', include(contract_router.urls)),
    path('', include(event_router.urls)),
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('signup/', RegisterApi.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from project.views import ProjectViewset
from user.views import RegisterApi #UserViewset
from issue.views import IssueViewset
from comment.views import CommentViewset
from contributor.views import ContributorViewset


# création du routeur
router = routers.SimpleRouter()
# déclaration de project afin de générer l'URL correspondante

projects_router = routers.SimpleRouter(trailing_slash=False)
projects_router.register(r"projects/?", ProjectViewset, basename="projects")

users_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
users_router.register(r"users/?", ContributorViewset, basename="users")

issues_router = routers.NestedSimpleRouter(projects_router, r"projects/?", lookup="projects", trailing_slash=False)
issues_router.register(r"issues/?", IssueViewset, basename="issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues/?", lookup="issues", trailing_slash=False)
comments_router.register(r"comments/?", CommentViewset, basename="comments")


urlpatterns = [
    path("", include(projects_router.urls)),
    path("", include(users_router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comments_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),    
    path('signup/', RegisterApi.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('', include(router.urls)), # urls du router pour rendre les urls disponibles
    #path('', include('user.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""