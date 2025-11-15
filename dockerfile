FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install pytest-html && pip install -r requirements.txt
COPY . .
CMD ["pytest","-v", "--html=Reports/report.html"]