# -*- coding: utf-8 -*-

def Raclette(ingredients, materiel):
    print("\nComment cuisiner la Raclette ?\n")
    
    while True:
        for i in ingredients:
            print(f"- {i}")
        for i in materiel:
            print(f"- {i}")
        break
    print("Voilà !\n")

Raclette(["fromage à raclette", "pommes de terre", "charcuterie", "cornichons"], ["casserole", "grille", "assiette"])
