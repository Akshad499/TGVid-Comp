#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("25271554", cast=int)
    API_HASH = config("cf9936ecab34ec6f25be13dd4bca3eaa")
    BOT_TOKEN = config("6621913506:AAFmQjHVpAhVhPfFVcKc4utnFK6j9-miVbw")
    DEV = 1664850827
    OWNER = config("5236678934")
    ffmpegcode = ["-map 0 -c:v libx264 -pix_fmt yuv420p -crf 30 -preset veryfast -s 856x480 -c:a aac -b:a 50k -c:s copy"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/BREEZE-HERE-02-11")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
