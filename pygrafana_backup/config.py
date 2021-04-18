import os

SERVER = os.environ['https://localhost:3000']
API_KEY = os.environ['eyJrIjoiNTI0WEJzSmExWnk0cHRuTWNiTm5IVkt2bVk2cUNZZ1giLCJuIjoiQmFja3VwIiwiaWQiOjF9']
HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
SSL_CHECK = False if os.environ.get('SSL_CHECK') is None else True
