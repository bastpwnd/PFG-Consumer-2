FROM python
COPY PFG-Consumer-2.py /PFG-Consumer-2.py
RUN pip install kafka-python
RUN pip install mysql-connector-python
CMD ["python","/PFG-Consumer-2.py"]




