FROM gitpod/workspace-full:latest

RUN echo "alias ll='ls -lrta'" >> ~/.bashrc
RUN echo "export PIP_USER=false" >> ~/.bashrc
