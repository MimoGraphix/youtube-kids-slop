import time

import requests


def clean_language(language):
    return (language
            .replace('\n', '')
            .replace(' ', '')
            .replace('-', '')
            .replace('ʼ', '')
            .replace('ǃ', '')
            .replace('\'', '')
            .replace('ä', 'a')
            .replace('ã', 'a')
            .replace('á', 'a')
            .replace('ç', 'c')
            .replace('é', 'e')
            .replace('ì', 'i')
            .replace('ñ', 'n')
            .replace('õ', 'o')
            .replace('ó', 'o')
            )


if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS

    names = [
        "MultiDOGIRLS",
        "BaRaDa",
        "BaRaDaGold",
        "DaRaDa",
        "MultiDo",
        "MultiDOChallenge",
        "MultiDOTeam",
        "YipYap",
        "HaHaNom",
    ]

    founded = open('results.txt', 'w')

    with open('languages.txt', 'r') as file:
        for language in file:

            language = clean_language(language)
            print('\033[34m' + "Language: " + language + '\033[0m')

            for name in names:
                # https://www.youtube.com/@MultiDOGIRLSSerbian
                url = "https://www.youtube.com/@" + name + language

                result = requests.get(url)
                if result.status_code == 200:
                    print('\033[32m' + "Found: " + url + '\033[0m')
                    founded.write(url + "\n")

            time.sleep(5) # because I dont want a BAN :D

    founded.close()
