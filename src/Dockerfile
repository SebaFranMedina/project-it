FROM python:3.13-slim
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
COPY extract-data.py .
 
CMD ["python", "extract-data.py"]
 