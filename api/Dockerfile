FROM python:3.11-alpine

WORKDIR /app

# Explicitly copy the requirements.txt from the build context.
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]