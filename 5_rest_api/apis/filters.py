import django_filters

from apis.models import School, ClassRoom, Teacher, Student

# code here

class SchoolFilter(django_filters.FilterSet):

    class Meta:
        model = School
        fields = {
            'school_name',
        }

class ClassRoomFilter(django_filters.FilterSet):

    class Meta:
        model = ClassRoom
        fields = {
            'school_id',
        }

class TeacherFilter(django_filters.FilterSet):

    class Meta:
        model = Teacher
        fields = {
            'school_id',
            'class_id',
            'first_name',
            'last_name',
            'gender'
        }

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = {
            'school_id',
            'class_id',
            'first_name',
            'last_name',
            'gender'
        }
