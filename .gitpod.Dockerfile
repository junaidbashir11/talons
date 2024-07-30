FROM gitpod/workspace-python

# Install the desired Python version (replace 3.x.y with your desired version)
RUN pyenv install 3.10.12
RUN pyenv global 3.10.12