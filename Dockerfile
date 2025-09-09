FROM python:3.11-slim

WORKDIR /app

# copy package and app
COPY setup.py requirements.txt /app/
COPY planner /app/planner
COPY app.py /app/

# install
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir .

# Expose port and run
ENV PORT 8080
EXPOSE 8080
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "--workers", "2"]