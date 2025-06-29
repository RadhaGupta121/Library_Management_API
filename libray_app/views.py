from django.shortcuts import render
from rest_framework import generics,status,serializers
from .models import Books,Author,students,Audit
from .serializers import BookSerializer, AuthorSerializer, StudentSerializer,AuditSerializer
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.response import Response
from http import HTTPStatus
from django.utils import timezone
from datetime import timedelta
from rest_framework.permissions import AllowAny

# Create your views here.
class BooksList(generics.ListCreateAPIView):
    queryset=Books.objects.all()
    print(queryset.query)
    serializer_class=BookSerializer
    # permission_classes = [AllowAny]  # Temporarily allow all
    authentication_classes = []     # Temporarily remove auth


class AuthorList(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class getBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer
    Lookup_fields='id'

class deleteBooks(generics.DestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BookSerializer
    Lookup_field='id'

class allStudents(generics.ListCreateAPIView):
    queryset=students.objects.all()
    serializer_class=StudentSerializer

class getStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset=students.objects.all()
    serializer_class=StudentSerializer
    Lookup_fields='pk'

class getAudits(generics.ListAPIView):
    queryset=Audit.objects.all()
    serializer_class=AuditSerializer
    
class updateAudits(generics.RetrieveUpdateDestroyAPIView):
    queryset=Audit.objects.all()
    serializer_class=AuditSerializer
    Lookup_fields='student_id'

class requestbook(generics.CreateAPIView):
    queryset=Audit.objects.all()
    serializer_class=AuditSerializer
    permission_classes = [AllowAny]  
    def perform_create(self,serializer):
        with transaction.atomic():
            book=serializer.validated_data['books_borrowed']
            if book.quantity<=0:
                raise serializers.ValidationError('The book is unavailable now!')
            
            book.quantity-=1
            book.save()
            borrowed_date=timezone.now()
            return_date=borrowed_date+timedelta(days=30)
            serializer.save(borrowed_date=borrowed_date,return_date=return_date)






    
    
    
