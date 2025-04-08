ingredients: list = ["fromage", "pommes de terre", "charcuterie"]
materiel : list = ["appareil à raclette", "couteau", "assiette"]


def Raclette(ingredients, materiel):
    print("Raclette :")
    print("Ingrédients :")
    for ingredient in ingredients:
        print("-", ingredient)
    
    for item in materiel:
        print("-", item)
    
    print("Bon appétit : ")


Raclette(ingredients, materiel)
