
FROM YusrilRNLD/U-Bot:master

RUN git clone -b main https://github.com/YusrilRNLD/U-Bot /home/U-Bot/ \
    && chmod 777 /home/U-Bot \
    && mkdir /home/U-Bot/bin/

WORKDIR /home/U-Bot/

CMD [ "python3", "-m", "Userbot"]
