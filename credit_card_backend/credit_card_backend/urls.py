from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credit_cards/', include('credit_cards.urls')),  # Include your credit_cards app URLs
    path('', RedirectView.as_view(url='/credit_cards/')),  # Redirect root URL to /credit_cards/
]
