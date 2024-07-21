meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "IDK": "Bilmiyorum demek"
            }
            
kelime= input("kelime girin:")
if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("sözlükte yok")
