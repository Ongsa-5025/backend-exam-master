from rest_framework import serializers


# code here

from apis.models import School, ClassRoom, Teacher, Student

class SchoolCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"

    def getObjBySchoolName(inSchoolName):
        try:
            obj = School.objects.filter(school_name__icontains=inSchoolName)
            return obj
        except Exception as e:
            print('getObjBySchoolName Error: ', e)
            return None
        
    def create(self, valiedate_data):
        return School.objects.create(**valiedate_data)

class SchoolUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class ClassRoomCreateSerializer(serializers.ModelSerializer):
    # school_name = serializers.CharField(source="school_id.school_name")
    class Meta:
        model = ClassRoom
        fields = '__all__'

    def create(self, valiedate_data):
        return ClassRoom.objects.create(**valiedate_data)
    
    def getAllObj(class_id):
        obj = ClassRoom.objects.filter()
        return obj

class ClassRoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
    
    def update(self, valiedate_data):
        return ClassRoom.objects.update(**valiedate_data)


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, valiedate_data):
        return Teacher.objects.create(**valiedate_data)
    
    def getAllObj(inSchoolId):
        if inSchoolId:
            obj = Teacher.objects.filter(school_id=inSchoolId)
        else:
            obj = Teacher.objects.filter()
        return obj

class TeacherUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def update(self, valiedate_data):
        return Teacher.objects.update(**valiedate_data)

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, valiedate_data):
        return Student.objects.create(**valiedate_data)
    
    def getAllObj(inSchoolId):
        if inSchoolId:
            obj = Student.objects.filter(school_id=inSchoolId)
        else:
            obj = Student.objects.filter()
        return obj

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def update(self, valiedate_data):
        return Student.objects.update(**valiedate_data)