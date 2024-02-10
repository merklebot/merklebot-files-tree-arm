FROM ghcr.io/merklebot/hackathon-amd-image:master as build

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ARG TARGETOS
ARG TARGETARCH

ARG Version
ARG GitCommit
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r requirements.txt
COPY . .

CMD ["python3.8", "main.py"]
