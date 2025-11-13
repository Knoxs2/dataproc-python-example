FROM apache/spark-py:3.5.0
WORKDIR /app
COPY src/ ./src/
COPY requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["spark-submit", "src/transform_spark_job.py"]