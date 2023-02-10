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

    ## Django Multiple Database

    - Model.objects.using('db_name').all()
    
    1- make 
    
    DATABASES = {
        'default': {},
        'first': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'first_db',
            'USER': 'postgres',
            'PASSWORD': '20708077r',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

    DATABASE_ROUTERS = ['Routers.routers.AuthRouter']

    2. make routers folder --> https://docs.djangoproject.com/en/4.1/topics/db/multi-db/

    3. 
    py manage.py makemirations

    - when migrate you have speak to --database= ~~
        py manage.py migrate --database=first
        py manage.py createsuperuser --database=first
        first one for 'auth', 'contenttypes' (users and admin)

    4. second db
        1. add too databases 
            },
            'second_db': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'second.db.sqlite3', #### note 'second_db.db.sqlite3' not just 'db.sqlite3'
            }

        2. add new router
            DATABASE_ROUTERS = ['Routers.routers.Second_bd']

        3. handle router.py file with new database

        4. py manage.py makemirations

        5. py manage.py migrate --database=second_db

    5. third database
        1. add too databases 
            },
            'third_with_mysql':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'third_multiple_db',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '',
        }

        2. add new router
            DATABASE_ROUTERS = [, 'Routers.routers.Third_db']

        3. handle router.py file with new database

        4. py manage.py makemirations

        5. py manage.py migrate --database=third database



    -------------------------------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------------------------------

    # Transaction Atomicity ( code as one unit )
    

    ## act the block of code as a one unit don't save any query action until all successfully

    ---- bank transaction example:

        payor = user.objects.get(name=name)
        payor.balance -= money
        payor.save()

        payee = user.objects.get(name=name)
        payee.balance -= money
        payee.save()

        --- problem --> if payee don't exist, payor balance will decrease actually


        payor = users.objects.select_for_update().get(name=name)
        payee = users.objects.select_for_update().get(name=name)

        with transaction.atomic():
            ""
                This block execute as a unit
            ""
            payor.balance -= money
            payor.save()

            payee.balance -= money
            payee.save()



    -- How to use transaction atomic

        from django.db import transaction

        - as a decorator
        @transaction.atomic()

        - using as context manager:
        with transaction.atomic():
            name.object.get()

    ## This operations must be committed as a unit they are wrapped with our transaction


    ----------------------------------------------------------------------------------------------------------

    -- Django Aggregation

    we have products table and want to sum price for all items 
    we need to get average for sum of price
    
    from django.db.models import Sum
    
    Products.objects.aggregate(Sum('price'))
    >>> {'age__sum': 84}
    a = Products.objects.aggregate(Sum('price'))

    to change 'age__sum'
    a = Products.objects.aggregate(new_name=Sum('price'))
    >>> {'new_name': 84}

    a['new_name']
    >>> 84
    

    from django.db.models import Sum, Max, Min, Avg
    a = Products.objects.aggregate(Sum('price'), Avg('price'), Max('price'))

    
    >>> data = ItemA.objects.aggregate(new=Sum('age'), m=Avg('age'), p=Max('class_number'))
    >>> data
    {'new': 84, 'm': 16.8, 'p': 8}
    >>> data['p']
    8

    ----------------------------------------------------------------------------------------------------------

    -- import CSV(excel file) Data to model

    - $var = import-csv .\books.csv | ConvertTo-Json
    - $var | Add-Content -path "mydata.json"

    = Will create new file with json format

    - handel this json file
        "model": "book.book",
        "id": "1",
        "fields": {
            ~
            ~
            ~
        }

        ** Add 'fields' before fields

    - json file ready

    - py manage.py loaddate mydata.json

"""