from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH


class Mitarbeiter ():
    def __init__(self, name, gehaltsgruppe):   #init hat 2 underscores weil es "protected" ist, d.h. von aussen geschützt!
        self.name = name 
        self.gehaltsgruppe = gehaltsgruppe

class Pfleger(Mitarbeiter):
    def __init__(self, name, gehaltsgruppe):
        Mitarbeiter.__init__(self, name, gehaltsgruppe)

class Ärzte(Mitarbeiter):
    def __init__(self, name, gehaltsgruppe, fachgebiet):
        Mitarbeiter.__init__(self, name, gehaltsgruppe)
        self.fachgebiet = fachgebiet

Arzt = Dr. Dolittle ('Tierarzt', 1)
Pfleger = Hans ('Pfleger01', 1)

class Raum ():
    def __init___(self, desinfiktionsstatus):
        self.desinfiktionsstatus = desinfiktionsstatus

class Besenkammer(Raum):
    def __init__(self,desinfiktionsstatus, desinfizieren):
        Raum.__init__(self, desinfiktionsstatus)
        desinfizieren
