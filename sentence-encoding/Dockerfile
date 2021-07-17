FROM amazon/aws-lambda-python

ARG MODEL_DIR=./models

ENV SENTENCE_TRANSFORMERS_HOME=$MODEL_DIR
ENV TRANSFORMERS_CACHE=$MODEL_DIR
ENV TRANSFORMERS_VERBOSITY=error

RUN yum -y install gcc-c++

COPY requirements.txt requirements.txt
RUN pip install torch==1.8+cpu -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

COPY ./ ./

# Run test cases and this saves the transformer model in the container
RUN pip install pytest --no-cache-dir && pytest tests -s -vv

RUN chmod -R 0777 $MODEL_DIR

CMD [ "main.lambda_handler"]