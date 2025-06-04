from django.urls import path
from .views import register_view, login_view, student_dashboard, logout_view, admin_dashboard, view_books, support_view


urlpatterns = [
    path("register", register_view, name='register' ),
    path("login", login_view, name='login' ),
    path('dashboard/student', student_dashboard, name="student_dashboard"),
    path('logout/', logout_view, name='logout'),
    path('dashboard/admin', admin_dashboard, name="admin_dashboard"),
    path('books/', view_books, name='view_books'),
    path('support/', support_view, name= 'support')
]