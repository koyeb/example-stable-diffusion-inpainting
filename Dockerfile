FROM python:3.10
WORKDIR /app

# Copy the requirements file
COPY requirements.txt app.py

# Install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
ENV GRADIO_SERVER_NAME="0.0.0.0”
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT:-8000}
CMD ["python", "app.py"]