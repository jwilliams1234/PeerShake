from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  #path('simpleSearch/',views.simpleSearch,name="simplesearch")
  path('chromeExtensionBase/', views.chromeExtensionBase, name="chromeExtensionBase"),
  path('chromeExtension/', views.chromeExtension, name="chromeExtension"),
  # path('ays/', views.areYouSurePage, name="aysPage"),
  # path('aysred/', views.areYouSure, name='areYouSure'),
  path('comment/<str:title>', views.displayComment, name="comment"),
  path('thankyou/', views.thankyou, name="ty"),
  path('commentForm/<str:title>', views.displayCommentForm, name="dsf"),
  path('displayCommentEmail/<str:email>/<str:title>', views.displayCommentEmail, name="dce"),
  path('comment/<str:title>/all', views.displayAll, name="comAll"),
]