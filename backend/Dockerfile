# 
FROM python:3.11-alpine

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "3"]
