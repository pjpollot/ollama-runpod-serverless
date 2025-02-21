FROM --platform=linux/amd64 python:3.13-bookworm

ARG MODEL_NAME="llama3"

WORKDIR /workspace

RUN curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
RUN tar -C /usr -xzf ollama-linux-amd64.tgz

COPY requirements.txt handler.py install.sh startup.sh test_input.json ./

RUN pip install -U pip
RUN pip install -r requirements.txt

RUN chmod +x install.sh startup.sh 
RUN ./install.sh ${MODEL_NAME}

ENV MODEL_NAME=${MODEL_NAME}

CMD [ "./startup.sh" ]