# Set base image (host OS)
FROM python:3.9

EXPOSE 5000/tcp

COPY ./requirements.txt /app/requirements.txt

# Set the working directory in the container
WORKDIR /app

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app

ENTRYPOINT [ "python" ]

CMD ["main.py" ]