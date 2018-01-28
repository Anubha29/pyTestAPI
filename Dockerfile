FROM ubuntu:14.04

# Update
RUN apt-get -yqq update
RUN apt-get install -yqq python
RUN apt-get -yqq install python-pip

# Install app dependencies
#RUN pip install Flask
RUN pip install -r requirements.txt

# Install DB
RUN sqlite3 salaries.db
RUN .mode csv salaries
RUN .import employee_chicago.csv salaries
RUN .quit

# Bundle app source
COPY app.py /app.py

EXPOSE  5000
CMD ["python", "/app.py", "-p 5000"]
