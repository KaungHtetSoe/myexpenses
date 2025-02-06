from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_swagger.views import get_swagger_view
from expenses.views import CategoryViewSet, IncomeViewSet, ExpenseViewSet, UserViewSet, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'incomes', IncomeViewSet, basename="incomes")
router.register(r'expenses', ExpenseViewSet, basename="expenses")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view()),
]

# schema_view = get_swagger_view(title='Polls API')
# urlpatterns += [
#     path(r'docs/', schema_view),
# ]


from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer, BrowsableAPIRenderer

urlpatterns += [
    path(
        "openapi/",
        get_schema_view(
            title="My API",
            description="API documentation",
            version="1.0.0",
            renderer_classes=[JSONOpenAPIRenderer, BrowsableAPIRenderer],
        ),
        name="openapi-schema",
    ),
]