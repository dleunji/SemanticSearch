FROM dleunji/klue-sts-model
RUN apt-get update
RUN apt-get install -y supervisor
WORKDIR /workspace
COPY fastapi/ .
COPY streamlit/ .
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 8000
EXPOSE 8501
CMD ["supervisord"]