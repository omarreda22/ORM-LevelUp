from django.shortcuts import render
from django.db.models import Q

from .models import Student


def student_list(request):
    pass


"""
    >>> Q with OR:
    Student.objects.filter(
        Q (name__contains='s') |
        ~Q (name__contains='3') -> don't Q 
    )

    Q with And: -> meaing both equal true
    Student.objects.filter(
        Q (name__contains='s') &
        ~Q (name__contains='3') -> don't Q 
    )




    >>> exclude()  => Not     ---> exclude
    Student.objects.exclude(name__contains='2')
    <QuerySet [<Student: s1>, <Student: s3>, <Student: s4>, <Student: s5>]>




    >>> Signs
    >   ---> gt
    >=  ---> gte
    <   ---> lt     -> less than
    <=  ---> lte    -> less than and equal 

    Student.objects.filter(age__gt=18)



    >>> only()  -> Select spacific fields from models
    for better performance
    
    > Student.objects.all().only('age') 



    >>> raw()   -> The only way to running sql in django 
    sql = "SELECT * FROM students_student"
    Student.objects.raw(sql)



    >>> to limit
    Student.objects.raw(sql)[:3]

    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------

    >>> Inheritance

     - Abstract 
     - multi-table model Inheritance
     - Polymorphish

    * Abstract  -> using (class meta)
    it doesn't include in actual database 
    will doesn't display in admin 
    
    class Student(models.Model):
        name = models.CharField(max_length=125)
        age = models.IntegerField(default=6)

        def __str__(self):
            return self.name

        class Meta:
            abstract = True
            ordering = ['-name']


    class ItemA(Student):
        class_number = models.IntegerField()

        def __str__(self):
            return self.class_number

        class Meta(Student.Meta):
            ordering = ['class_number']


    class ItemB(Student):
        class_number_student = models.IntegerField()

        def __str__(self):
            return self.class_number_student

        class Meta(Student.Meta):
            ordering = ['class_number_student']

    ---------------------------------------------------
    * Inheritance  -> multi-table model Inheritance

    class StudentMultiTable(models.Model):
        name = models.CharField(max_length=125, blank=True, null=True)
        age = models.IntegerField(default=6, blank=True, null=True)

        def __str__(self):
            return self.name


    class MultiTable(StudentMultiTable):
        new_name = models.CharField(max_length=125, blank=True, null=True)


    ******* 

    >>> {{student.MultiTable.new_name}}
    
    student = StudentMultiTable.objects.all() --> is very bad we select every item individual

    student = StudentMultiTable.objects.all().select_related('MultiTable') --> is good, use join
    student = StudentMultiTable.objects.all().prefetch_related('MultiTable') --> is better then select related


    -------------------------------------------------------------------------------------------------------------

    ###### Django debug toolbar
    - System information
    - timing 
    - Setting/configuration
    - Header
    - SQL
    - Templates, includes

    = Provide us sql performance data
    
    ** he provide us really valuable information

    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------

    ## Better performance ## -------> V1(v11)
    # Setup Django debug toolbar to see performance for sql 
    # Inheritance [ Abstract - multi-table model Inheritance - Polymorphish ]
    # maybe best one Polymorphish

    # use [ .select_related()  -- .prefetch_related() ]

    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------



"""