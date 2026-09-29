meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap", 
    "GHOST": "görmezden gelmek",
    "SHEESH": "onaylamamak",
    "ROFL": "bir şakaya karşılık cevap"
            }
word = input("anlamadiginiz bir kelime yazin: ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("boyle bir kelime yok")
