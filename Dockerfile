FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create working directory
RUN mkdir -p /hello-action

# Install dependencies
ADD requirements.txt /hello-action/requirements.txt
RUN apk add --no-cache git && pip3 install -r /hello-action/requirements.txt

# Configure git
RUN git config --global user.name "hello-bot"
RUN git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"

# Add main script
ADD hello.py /hello-action/hello.py

# Set entrypoint
ENTRYPOINT ["python3", "/hello-action/hello.py"]

