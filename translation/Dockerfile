FROM amazon/aws-lambda-python

RUN mkdir /cache
RUN mkdir /cache/easynmt
RUN mkdir /cache/transformers
RUN mkdir /cache/torch

ENV EASYNMT_CACHE=/cache/easynmt
ENV TRANSFORMERS_CACHE=/cache/transformers
ENV TRANSFORMERS_VERBOSITY=error
ENV TORCH_CACHE=/cache/torch

RUN yum -y install gcc-c++

COPY requirements.txt requirements.txt
RUN pip install torch==1.8+cpu -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir\
    && python -m nltk.downloader 'punkt'

COPY ./ ./

# Run test cases and this saves the transformer model in the container
# RUN pip install pytest --no-cache-dir && pytest tests -s -vv

RUN chmod -R 0755 /cache/easynmt
RUN chmod -R 0755 /cache/transformers
RUN chmod -R 0755 /cache/torch

CMD [ "lambda/main.lambda_handler"]