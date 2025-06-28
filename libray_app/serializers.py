from rest_framework import serializers
from .models import Books,Author,students,Audit

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields='__all__'

class AuditSerializer(serializers.ModelSerializer):
    student_name=serializers.StringRelatedField(source='student',read_only=True)
    books=serializers.StringRelatedField(source='books_borrowed',read_only=True)
    class Meta:
        model=Audit
        fields=['books_borrowed','books','student_name','student','borrowed_date','return_date','penality']
        read_only_fields=['borrowed_date','return_date']

