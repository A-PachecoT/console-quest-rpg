import subprocess
import time
import requests

if __name__ == "__main__":
	api_process = subprocess.Popen(['python', 'app/api_app.py'])

	while True:
		try:
			# Try making a GET request to the health check endpoint
			response = requests.get("http://localhost:8000/health")
			if response.status_code == 200:
				print("API is up!")
				break;
		except requests.ConnectionError:
			print("Waiting for the API to start...")
		time.sleep(1)

	client_process = subprocess.Popen(['python', 'app/client_app.py'])

	api_process.wait()
	client_process.wait()