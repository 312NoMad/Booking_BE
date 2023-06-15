# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements .
RUN pip install -r requirements/prod.txt

# Copy the project code to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Gunicorn configuration
COPY gunicorn.conf.py /app

# Expose the port for Gunicorn
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "Booking_BE.wsgi:application"]
