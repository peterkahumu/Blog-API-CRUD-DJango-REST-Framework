from  django.urls import path
from .views import UserViewSet, PostViewset # PostDetail, PostList, UserDetail, Userlist

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet,basename='users')
router.register('', PostViewset, basename='post')

urlpatterns = router.urls

# urlpatterns = [
#     path("<int:pk>/", PostDetail.as_view(), name='post_detail'),
#     path('', PostList.as_view(), name='post_list'),
#     path('users/', Userlist.as_view(), name='user_list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail')
# ]