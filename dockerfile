FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /dir1
WORKDIR /dir1
COPY requirements.txt /dir1/
RUN pip install -r requirements.txt
COPY ./ /dir1/
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

