# path si se utiliza para poder levantar las rutas y debemos import las vistas que van a responder a estas url
from django.urls import path
from .views import home,about,post,skill_detail

#siempre debemos poner nombre el nombre de la aplicacion
#path('url','class o def que deceamos que responda a esa url')
#name='nombre de la ruta, me permite redireccionarme a otra pagina desde la url 

app_name='core'
urlpatterns = [
    path('', home,name='home'),
    path('about/',about,name='about'),
    path('post/',post,name='post'),
    path('detail/<cod>',skill_detail,name='skill_detail'),
]
