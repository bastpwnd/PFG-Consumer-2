FROM python
COPY kafka/PFG-Consumer-2.py /PFG-Consumer-2.py
COPY infrastructure/DataBase.py /infrastructure/DataBase.py
RUN pip install kafka-python
RUN pip install mysql-connector-python
CMD ["python","/PFG-Consumer-2.py"]




