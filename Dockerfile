
FROM yusrilrnld/u-bot:master
# ======================
#    U-BOT DOCKER
#   FROM DOCKERHUB.COM
# ======================
RUN git clone -b master https://github.com/YusrilRNLD/U-Bot home/yusgans/
WORKDIR home/yusgans/
CMD ["python3", "-m", "userbot"]
