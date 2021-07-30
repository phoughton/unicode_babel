FROM python:3.9

ENV PIP_USER=false 

RUN echo "alias ll='ls -lrta'" >> ~/.bashrc
