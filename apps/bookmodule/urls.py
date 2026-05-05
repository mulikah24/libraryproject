from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/links', views.links),
    path('html5/text/formatting', views.formatting),
    path('html5/listing', views.listing),
    path('html5/tables', views.tables),
    
    path('search', views.search_books),
    
    path('insert', views.insert_books),

    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),

    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),

    path('lab9/task1', views.lab9task1),
    path('lab9/task2', views.lab9task2),
    path('lab9/task3', views.lab9task3),
    path('lab9/task4', views.lab9task4),
    path('lab9/task5', views.lab9task5),
    path('lab9/task6', views.lab9task6),
    
    path('lab10_part1/list', views.list, name='list'),
    path('lab10_part1/add', views.add, name='add'),
    path('lab10_part1/edit/<int:id>', views.edit, name='edit'),
    path('lab10_part1/delete/<int:id>', views.delete, name='delete'),
    
    path('lab10_part2/list2', views.list2, name='list2'),
    path('lab10_part2/add2', views.add2, name='add2'),
    path('lab10_part2/edit2/<int:id>', views.edit2, name='edit2'),
    path('lab10_part2/delete2/<int:id>', views.delete2, name='delete2'),
    
    
    path('lab11/add_book', views.add_book, name='add_book'),
    path('lab11/add_book_image/', views.add_book_image, name='add_book_image'),



     path('lab13/', views.lab13),

]
