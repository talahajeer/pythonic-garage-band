from abc import abstractclassmethod

class Musician:
    members = []
    def __init__(self,name):
       
        self.name = name
        Musician.members.append(self)




    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass
    @abstractclassmethod
    def get_instrument(self):
        pass
    @abstractclassmethod
    def play_solo(self):
        pass

    

class Guitarist(Musician):

    def __str__(self) :

        return "My name is {} and I play guitar".format(self.name)

    def __repr__(self):

        return "Guitarist instance. Name = {}".format(self.name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"




# if __name__=="__main__":
#     pass



class Drummer(Musician):
     def __str__(self) :

        return "My name is {} and I play drums".format(self.name)

     def __repr__(self):

        return "Drummer instance. Name = {}".format(self.name)
     def get_instrument(self):
        return "drums"

     def play_solo(self):
        return "rattle boom crash"

class Bassist(Musician):
   def __str__(self) :

        return "My name is {} and I play bass".format(self.name)

   def __repr__(self):

        return "Bassist instance. Name = {}".format(self.name)
        
   def get_instrument(self):
        return "bass"

   def play_solo(self):
        return "bom bom buh bom"


class Band(Musician):
    def __init__(self,name,members):
       
        self.name = name
        self.members = members

    def play_solos(self):
        solos = []
        for member in Band.members:
            print(member.play_solo())
            solos.append(member.play_solo())
        print(solos)
        return solos

    


one_band = Band(
        "Nirvana",
        [Guitarist("Kurt Cobain"), Bassist("Krist Novoselic"), Drummer("Dave Grohl"),],
    )



solos = one_band.play_solos()
# # print(solos) 
# # print(solos[0])
# print(len(solos))