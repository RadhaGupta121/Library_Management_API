from django.contrib import admin
from django.urls import path
from .views import BooksList,AuthorList,getBooks,deleteBooks,allStudents,getStudents,getAudits,updateAudits,requestbook

urlpatterns = [
    path('allbooks',BooksList.as_view(),name='allbooks' ),
    path('allauthors',AuthorList.as_view(),name='allauthors'),
    path('getbooks/<int:pk>',getBooks.as_view(),name='getBooks'),
    path('delete/<int:pk>',deleteBooks.as_view(),name='deleteBooks'),
    path('allstudents',allStudents.as_view(),name='allStudents'),
    path('getstudents/<int:pk>',getStudents.as_view(),name='getStudents'),
    path('getAudits',getAudits.as_view(),name='getAudits'),
    path('updateAudits/<int:pk>',updateAudits.as_view(),name='updateAudits'),
    path('requestbook/',requestbook.as_view(),name='requestbook')
]
