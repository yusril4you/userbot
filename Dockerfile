
#yusrilrnld
RUN git clone -b ubot https://github.com/yusrilrnld/ubot /home/ubot/ \
    && chmod 777 /home/ubot \
    && mkdir /home/ubot/bin/

COPY ./sample_config.env ./config.env* /home/ubot/

WORKDIR /home/ubot/

CMD [ "python3", "-m", "Userbot"]
