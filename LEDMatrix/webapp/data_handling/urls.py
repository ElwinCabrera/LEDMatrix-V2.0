from django.urls import path, include
from .data import  fetch_drawing, fetch_drawing_admin, new_drawing, save_drawing, submit_drawing, delete_drawing, add_to_curr_showing_list, remove_from_showing_list, remove_from_new_subms_list
from .tasks import start_tasks
urlpatterns = [
    
    path('fetch-drawing/', fetch_drawing, name="fetch_drawing"),
    path('new-drawing/', new_drawing, name="new_drawing"),
    path('save-drawing/', save_drawing, name="save_drawing"),
    path('submit-drawing/', submit_drawing, name="submit_drawing"),
    path('delete-drawing/', delete_drawing, name="delete_drawing"),
    path('admin-data/fetch-drawing/', fetch_drawing_admin, name="fetch_drawing_admin_dash"),
    path('admin-data/add-to-showing-list/', add_to_curr_showing_list, name="add_to_curr_showing_list"),
    path('admin-data/remove-from-showing-list/', remove_from_showing_list, name="remove_from_showing_list"),
    path('admin-data/remove-from-new-subms-list/', remove_from_new_subms_list, name="remove-from-showing-list"),
    
]

# I put this in here because this file (urls.py) django only runs it once and we only want to start our tasks once
#start_tasks()