from requests import get

websites = [
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
]

for web in websites:
  if not web.startswith("https://"):
    web = f"https://{web}"
  response = get(web)
  print(response.status_code)