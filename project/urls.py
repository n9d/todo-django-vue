from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from todo.urls import router as todo_router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include(todo_router.urls)),
    path('', TemplateView.as_view(template_name='templates/index.html'), name='index'),
]
