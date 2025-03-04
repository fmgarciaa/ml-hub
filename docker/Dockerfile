FROM python:3.9.21-slim

# Define user variables
ARG NB_USER=jupyter
ARG NB_UID=1000
ARG NB_GID=100

# Avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and clean cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Verify Node.js and npm installation
RUN node -v && npm -v

# Install configurable-http-proxy
RUN npm install -g configurable-http-proxy --unsafe-perm=true

# Create a non-root user for JupyterHub
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

# Set working directory
WORKDIR /home/$NB_USER

# Copy necessary files before installing dependencies
COPY requirements.txt /tmp/requirements.txt
COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

# Install JupyterHub and dependencies efficiently
RUN pip install --no-cache-dir jupyterhub jupyterlab notebook \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

# Create notebooks directory and set permissions
RUN mkdir -p /home/$NB_USER/notebooks && chown -R $NB_USER:$NB_GID /home/$NB_USER

# Switch to non-root user for security
USER $NB_USER

# Expose JupyterHub port
EXPOSE 8000

# Start JupyterHub
CMD ["jupyterhub", "--config", "/etc/jupyterhub/jupyterhub_config.py"]

