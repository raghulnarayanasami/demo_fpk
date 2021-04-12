FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /root
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
COPY ./ /root/
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

