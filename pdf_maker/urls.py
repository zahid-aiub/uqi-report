from django.contrib import admin
from django.urls import path
from rest_framework import routers


from pdf.views import pdf_generate_from_url, pdf_generate_from_html, json_to_html, json_to_csv, json_to_xls

router = routers.DefaultRouter()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('url-to-pdf/', pdf_generate_from_url),
    path('html-to-pdf/', pdf_generate_from_html),
    path('json-to-html/', json_to_html),
    path('json-to-csv/', json_to_csv),
    path('json-to-xls/', json_to_xls),
]

urlpatterns += router.urls
