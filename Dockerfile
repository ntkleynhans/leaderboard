FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN python3 -m pip install -r requirements.txt
CMD ["ranking_table.py"]
ENTRYPOINT ["python3"]