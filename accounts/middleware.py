from django.shortcuts import redirect
from django.urls import reverse


class RedirectLoggedInMiddleware:
    """Redirect logged in users from login page."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check path and redirect
            if request.path == reverse("login") or request.path == reverse(
                "password_reset"
            ):
                return redirect("dashboard")
        return self.get_response(request)
