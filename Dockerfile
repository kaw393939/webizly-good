FROM python:3.11.1-slim-bullseye
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
ENV FLASK_APP=wsgi.py
ENV PORT=8080
ENV DEPLOYMENT=production
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
RUN pip3 install -r requirements.txt
RUN chmod u+x ./production.sh
CMD ["./production.sh"]

# CMD ["runuser", "-u", "myuser", "--", "python", "-m", "flask", "run", "--host=0.0.0.0"]