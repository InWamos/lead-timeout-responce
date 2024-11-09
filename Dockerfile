FROM python:3.10-slim

WORKDIR /app

# Copy the application code
COPY . /app

# Install virtualenv
RUN python -m venv /venv

# Install dependencies
RUN /venv/bin/pip install -r requirements.txt

# Set the PATH to include the virtual environment
ENV PATH="/venv/bin:$PATH"

# Run the application
CMD ["/venv/bin/python", "src/__main__.py"]