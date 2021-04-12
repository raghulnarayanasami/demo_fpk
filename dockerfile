FROM python:3
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./root
RUN pip install -r ./root/requirements.txt
COPY ./ ./root
EXPOSE 80
WORKDIR /root
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

