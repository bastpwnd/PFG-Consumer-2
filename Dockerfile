FROM python
COPY kafka/Consumer-2.py /Consumer-2.py
COPY infrastructure/DataBase.py /infrastructure/DataBase.py
RUN pip install kafka-python
RUN pip install mysql-connector-python
CMD ["python","/Consumer-2.py"]




