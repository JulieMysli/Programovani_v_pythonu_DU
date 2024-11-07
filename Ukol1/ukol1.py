import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def __str__(self):
        return (f"Pozemek: {self.estate_type}, lokalita: {self.locality.name} (koeficient {self.locality.locality_coefficient}), "
                f"rozloha: {self.area} metrů čtverečních, daň: {self.calculate_tax()} Kč.")
    
    def calculate_tax(self):
        tax = self.area * estate_type[self.estate_type] * self.locality.locality_coefficient
        return math.ceil(tax)
    
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def __str__(self):
        if self.commercial:
            property_type = "komerční"
        else:
            property_type = "bytová"
        return (f"Stavba: {property_type}, lokalita: {self.locality.name} (koeficient {self.locality.locality_coefficient}), "
                f"rozloha: {self.area} metrů čtverečních, daň: {self.calculate_tax()} Kč.")

    def calculate_tax(self):
        tax = self.area * self.locality.locality_coefficient * 15
        if self.commercial == True:
            tax *= 2
        return math.ceil(tax)
    
    
estate_type = {"land": 0.85, "building site": 9, "forrest": 0.35, "garden": 2}


# Locality
locality_manetin = Locality("Manětín", 0.8)
locality_brno = Locality("Brno", 3)


# Property
agricultural_land = Estate(locality_manetin,"land", 900)
house = Residence(locality_manetin, 120)
office = Residence(locality_brno, 90, True)


print(agricultural_land.calculate_tax()) 
print(house.calculate_tax())
print(office.calculate_tax())

print(agricultural_land)
print(house)
print(office)




















# # print(locality_manetin) 

# # Když jsem zadala tohle, házelo mi to chybu: # <__main__.Locality object at 0x00000220071AAF90>
# # Tato chyba znamená, že se ti zobrazil výchozí výpis objektu třídy Locality místo toho, abys viděla název 
# # nebo koeficient lokality, které jsi chtěla. Výpis jako <__main__.Locality object at 0x00000220071AAF90> 
# # ti říká, že Python vidí tento objekt jako instanci třídy Locality uloženou na určité adrese v paměti, 
# # ale neví, jak ho má „hezky“ zobrazit.

# # Aby se při výpisu objektu zobrazily konkrétní informace, například název lokality nebo její koeficient, 
# # je dobré do třídy Locality přidat speciální metodu __str__ nebo __repr__, která určuje, jak se objekt má zobrazit:

# class Locality:
#     def __init__(self, name, locality_coefficient):
#         self.name = name
#         self.locality_coefficient = locality_coefficient
    
#     def __str__(self):
#         return f"Locality: {self.name}, Koeficient: {self.locality_coefficient}"

# S touto metodou, když zavoláš print(locality_manetin), vypíše se:

# # Locality: Manětín, Koeficient: 0.8