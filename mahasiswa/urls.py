from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [ path('daftar/', views.daftar_mahasiswa, name='daftar_mahasiswa'), 
                path('tambah/', views.tambah_mahasiswa, name='tambah_mahasiswa'),
                path('edit/<int:id>/', views.edit_mahasiswa, name='edit_mahasiswa'),
                path('hapus/<int:id>/', views.hapus_mahasiswa, name='hapus_mahasiswa'),
                path('', RedirectView.as_view(url='daftar/')),
            ]

path('', views.index, name='index'),
