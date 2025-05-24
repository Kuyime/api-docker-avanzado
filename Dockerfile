FROM python:3.11-slim
WORKDIR /app
COPY app/ /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "main.py"]