from django.urls import path

from . import views

urlpatterns = [
    path("",
        view=views.QuestionsView.as_view(), name="index"),
    path('<int:question_id>/', views.question_detail, name='detail'),
]
