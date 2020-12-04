FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["ranking_table.py"]
ENTRYPOINT ["python3"]