class GestionCpt8:
    def __init__(self, compte, nom, soldeCompte):
       self.compte=compte
       self.nom=nom
       self.soldeCompte=soldeCompte
    def Versement(self,sommeV):
        self.soldeCompte=self.soldeCompte+sommeV
        return self.soldeCompte
    def Retrait(self, sommeR):
        if(self.soldeCompte>=sommeR):
           self.soldeCompte=self.soldeCompte-sommeR
           return self.soldeCompte
        else:
            print("Le solde actuel de votre compte est insuffisant")
    def affichageInfo(self):
        print("Le numéro de votre compte est: ", self.compte)
        print("Le nom du client est: ", self.nom)
        print("Le solde de votre compte est: ", self.soldeCompte)
#test de la classe
client1=GestionCpt8(12345678,"Lipo",10000)
client1.Versement(20000)
client1.affichageInfo()
print("-------------------------")
client2=GestionCpt8(12345678,"Lipo",20000)
client2.Retrait(25000)
client2.affichageInfo()




        
    
        
        
        

