from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import redirect
from django.conf import settings
import urllib.parse

def spotify_auth(request):
    scope = "user-read-private user-read-email"
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "scope": scope,
    }
    url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    return redirect(url)


import requests
from django.http import JsonResponse

def spotify_callback(request):
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "No code provided"}, status=400)

    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "client_secret": settings.SPOTIFY_CLIENT_SECRET,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(token_url, data=payload, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        # Save token_data to session or DB (access_token, refresh_token, expires_in)
        return JsonResponse(token_data)
    else:
        return JsonResponse({"error": "Token exchange failed", "details": response.json()}, status=500)



