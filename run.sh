docker build -t fastapi-app .       
docker run -v /Users/k/Desktop/fastapi:/app  -p8000:8000 -d fastapi-app