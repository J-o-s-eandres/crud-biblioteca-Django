from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns=[#acceso a las vistas 
    path('',views.inicio,name='inicio'),#views.nombreDeLaVista
    #path('nosotros',views.nosotros,name='nosotros'),
    path('libros',views.libros,name='libros'),
    path('libros/crear',views.crear,name='crear'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('libros/editar/<int:id>',views.editar,name='editar'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
