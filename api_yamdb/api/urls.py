from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('v1/', include('api.v1.urls'))
]
# 3 123123
