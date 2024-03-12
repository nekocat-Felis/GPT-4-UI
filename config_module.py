# config.txt から各種設定を読み込むモジュール

with open("config.txt", encoding="utf-8") as f:
    config_text = f.readlines()

config_dict = {}
for row in config_text:
    words = row.split("#")[0].split("=")
    if (len(words) == 2):
        config_dict[words[0].strip()] = words[1].strip()