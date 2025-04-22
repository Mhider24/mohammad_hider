FROM mcr.microsoft.com/devcontainers/universal:2-linux
# Install the xz-utils package
RUN apt-get update && apt-get install -y xz-utils

# Install Python packages (Flask)
RUN pip install flask

# Install Node.js and Vue CLI globally
RUN npm install -g @vue/cli