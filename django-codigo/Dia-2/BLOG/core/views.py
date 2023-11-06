from django.shortcuts import render
from .models import Persona,Skill,Post
# Create your views here.
#para poder obtener la inf de los modelos y podemos mostarlos debemos importar

# ya hemos creado los modelos - template - vistas - ruta(url)

#crea una vista que es una funcion que va a retornar un template 
def home(request):
  template_name='index.html'
  #! return un arreglo de objetos todos n registros
  persona=Persona.objects.get(id=1)
  skill=Skill.objects.all()
  context={
    'per':persona ,
    'ski':skill
  }
  return render(request,template_name,context)


def about(request):
  template_name='about.html'
  persona= Persona.objects.get(id=1)
  context={
    'per':persona
  }
  return render(request,template_name,context)


def post(request):
  template_name='post.html'
  persona=Persona.objects.get(id=1)
  post=Post.objects.all()
  context={
    'per':persona,'post':post
  }
  return render(request,template_name,context)


def skill_detail(request,cod):
  template_name='skill_detail.html'
  persona=Persona.objects.get(id=1)
  skillDetail=Skill.objects.get(codigo=cod)
  context={
    'per':persona,'skill':skillDetail
  }
  return render(request,template_name,context)