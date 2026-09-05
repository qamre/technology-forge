FROM python:3.7-alpine

#add user group and ass user to that group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

#creates work dir
WORKDIR /app
#copy python script to the container folder app
COPY helloworld.py /app/helloworld.py
RUN chmod +x /app/helloworld.py
#user is appuser
USER appuser
ENTRYPOINT ["python", "/app/helloworld.py"]
