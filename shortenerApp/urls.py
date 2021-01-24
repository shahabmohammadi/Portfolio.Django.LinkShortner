from django.urls import path

from shortenerApp.views import HomeView, LinkView, AnalysisView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:store_id>/', LinkView.as_view(), name='link'),
    path('statistic/<int:store_id>/', StatisticView.as_view(), name='statistic'),
]
