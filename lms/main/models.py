from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    skills = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "1. Teachers"
        
    def __str__(self):
        return self.full_name
    
        
        
    
class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    
    class Meta:
        verbose_name_plural = "2. Course Categories"
        
    def __str__(self):
        return self.title
    
    
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    featured_image = models.ImageField(upload_to='course_imgs/', null=True)
    technologies = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "3. Courses"
        
    def __str__(self):
        return self.title
    
        
        
    
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    interested_categories = models.TimeField(max_length=255)
    
    class Meta:
        verbose_name_plural = "4. Students"
        
    def __str__(self):
        return self.full_name
    
    