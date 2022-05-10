
RUN git clone -b main https://github.com/yusril4you/ubot /home/ubot/ \
    && chmod 777 /home/ubot \
    && mkdir /home/ubot/bin/

WORKDIR /home/ubot/

CMD [ "python3", "-m", "Userbot"]
