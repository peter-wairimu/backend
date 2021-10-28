from .models import User,Courses
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer,CoursesSerializer
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
class LoginAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data

		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})

class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		print(request.data)
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		return Response({
			'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})


class UserAPI(generics.RetrieveAPIView):
	permission_classes = [
		permissions.IsAuthenticated
	]
	serializer_class = UserSerializer

	def get_object(self):
		self.request.user



@csrf_exempt
def  coursesApi(request,id=0):
    if request.method == 'GET':
        courses = Courses.objects.all()
        courses_serializer = CoursesSerializer(courses,many=True)
        return JsonResponse(courses_serializer.data,safe=False)

    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serializer = CoursesSerializer(data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("Successfully added",safe=False)
        return JsonResponse("Failed to upload",safe=False)

    elif request.method == 'PUT':
        course_data = JSONParser().parse(request)
        course = Courses.objects.get(courseId = course_data ["courseId"])
        course_serializer = CoursesSerializer(course,data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("Successfully updated",safe=False)
        return JsonResponse("Sorry the update was not succesfull try again",safe=False)


    elif request.method == "DELETE":
        course = Courses.objects.get(courseId=id)
        course.delete()
        return JsonResponse("Deleted Successfully",safe=False)

        

