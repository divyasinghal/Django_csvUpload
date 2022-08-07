from django.urls import path
#now import the views.py file into this code
from . import views
from upload.views import storeData_upload,filterData,saveStoreData

urlpatterns=[
  path('', storeData_upload, name="storeData_upload"),
  path('filterData/<int:id>',filterData,name="filterData"),
  path('saveStoreData/<int:id>',saveStoreData,name="saveStoreData")
]