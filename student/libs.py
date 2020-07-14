from .models import Student
from .serializers import StudentSerializer

def get_students(query = {}):
    students = Student.objects.filter(**query)
    serializer = StudentSerializer(students, many = True)
    return serializer.data

def get_student_by_uuid(uuid):
    student = Student.objects.get(uuid = uuid)
    serializer = StudentSerializer(student)
    return serializer.data

def delete_student(uuid):
    try:
        student = Student.objects.get(uuid = uuid).delete()
        return True
    except Exception as e:
        raise e

def create_student(data):
    new_student = StudentSerializer(data = data)
    if new_student.is_valid():
        new_student.save()
        return {'success': True, 'student':new_student.data}
    else:
        return {'success': False, 'error':new_student.errors}


def update_student(uuid, data):
    pass
