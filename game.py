
class App(object):

    def __init__(self):

        self.depList = [["01", "Ain"],
                   ["02", "Aisne"],
                   ["03", "Allier"],
                   ["04", "Alpes-de-Haute-Provence"],
                   ["05", "Hautes-alpes"],
                   ["06", "Alpes-maritimes"],
                   ["07", "Ardèche"],
                   ["08", "Ardennes"],
                   ["09", "Ariège"],
                   ["10", "Aube"],
                   ["11", "Aude"],
                   ["12", "Aveyron"],
                   ["13", "Bouches-du-Rhône"],
                   ["14", "Calvados"],
                   ["15", "Cantal"],
                   ["16", "Charente"],
                   ["17", "Charente-maritime"],
                   ["18", "Cher"],
                   ["19", "Corèze"],
                   ["2A", "Corse-du-Sud"],
                   ["2B", "Haute-Corse"],
                   ["21", "Côte-d'Or"],
                   ["22", "Côtes-d'Armor"],
                   ["23", "Creuse"],
                   ["24", "Dordogne"],
                   ["25", "Doubs"],
                   ["26", "Drôme"],
                   ["27", "Eure"],
                   ["28", "Eure-et-loir"],
                   ["29", "Finistère"],
                   ["30", "Gard"],
                   ["31", "Haute-garonne"],
                   ["32", "Gers"],
                   ["33", "Gironde"],
                   ["34", "Hérault"],
                   ["35", "Ille-et-vilaine"],
                   ["36", "Indre"],
                   ["37", "Indre-et-loire"],
                   ["38", "Isère"],
                   ["39", "Jura"],
                   ["40", "Landes"],
                   ["41", "Loir-et-cher"],
                   ["42", "Loire"],
                   ["43", "Haute-loire"],
                   ["44", "Loire-Atlantique"],
                   ["45", "Loiret"],
                   ["46", "Lot"],
                   ["47", "Lot-et-garonne"],
                   ["48", "Lozère"],
                   ["49", "Maine-et-loire"],
                   ["50", "Manche"],
                   ["51", "Marne"],
                   ["52", "Haute-marne"],
                   ["53", "Mayenne"],
                   ["54", "Meurthe-et-moselle"],
                   ["55", "Meuse"],
                   ["56", "Morbihan"],
                   ["57", "Moselle"],
                   ["58", "Nièvre"],
                   ["59", "Nord"],
                   ["60", "Oise"],
                   ["61", "Orne"],
                   ["62", "Pas-de-calais"],
                   ["63", "Puy-de-dôme"],
                   ["64", "Pyrénées-atlantiques"],
                   ["65", "Hautes-Pyrénées"],
                   ["66", "Pyrénées-orientales"],
                   ["67", "Bas-rhin"],
                   ["68", "Haut-rhin"],
                   ["69", "Rhône"],
                   ["70", "Haute-saône"],
                   ["71", "Saône-et-loire"],
                   ["72", "Sarthe"],
                   ["73", "Savoie"],
                   ["74", "Haute-savoie"],
                   ["75", "Paris"],
                   ["76", "Seine-maritime"],
                   ["77", "Seine-et-marne"],
                   ["78", "Yvelines"],
                   ["79", "Deux-sèvres"],
                   ["80", "Somme"],
                   ["81", "Tarn"],
                   ["82", "Tarn-et-garonne"],
                   ["83", "Var"],
                   ["84", "Vaucluse"],
                   ["85", "Vendée"],
                   ["86", "Vienne"],
                   ["87", "Haute-vienne"],
                   ["88", "Vosges"],
                   ["89", "Yonne"],
                   ["90", "Territoire de berlfort"],
                   ["91", "Essonne"],
                   ["92", "Hauts-de-seine"],
                   ["93", "Seine-Saint-Denis"],
                   ["94", "Val-de-marne"],
                   ["95", "Val-d'oise"]]

        # parametrage de la fenetre
        self.root = Tk()
        self.root.title("Communes françaises")
        self.root.config(bg="#323232")

        self.color = "#323232"

        # lecture du ficher csv
        villes = open('villes_france.csv')
        fileCsv = csv.reader(villes)
        self.data = list(fileCsv)

        # definition de tous les frame

        self.frameTop = Frame(self.root, bg=self.color)
        self.frameTop.grid(row=0, column=0, pady=10, padx=20)
        self.frameMid = Frame(self.root, bg=self.color)
        self.frameMid.grid(row=1, column=0, pady=20, padx=20)
        self.frameBot = Frame(self.root, bg=self.color)
        self.frameBot.grid(row=2, column=0, pady=20, padx=20)

        self.frameBL = Frame(self.frameBot, bg=self.color)
        self.frameBL.grid(row=0, column=0)
        self.frameB = Frame(self.frameBot, bg=self.color)
        self.frameB.grid(row=0, column=1, padx=30)
        self.frameBR = Frame(self.frameBot, bg=self.color)
        self.frameBR.grid(row=0, column=2)

        # frame du haut de la fenetre

        self.scale = Scale(self.frameTop, length=400, orient=HORIZONTAL,
                           label="Nombre d'habitants minimum :", troughcolor='dark grey',
                           sliderlength=20, showvalue=1, from_=0, to=100000,
                           tickinterval=25000, bg=self.color, fg="white")
        self.scale.grid(row=0, column=0)

        self.scaleDep = Scale(self.frameTop, length=400, orient=HORIZONTAL,
                           label="Choisir département (si tous choisir 0) :", troughcolor='dark grey',
                           sliderlength=20, showvalue=1, from_=0, to=95,
                           tickinterval=20, bg=self.color, fg="white")
        self.scaleDep.grid(row=1, column=0)




        # frame du millieu de la fenetre
        self.labCity = Label(self.frameMid, bg=self.color, fg='white', font=("Helvetica", 30), width=40, justify="center")
        self.labCity.grid(row=0, column=0)

        Button(self.frameBR, text="Suivant", fg="#323232",command=self.load, font=("Helvetica", 30)).grid(row=0, column=0)

        # frame du bas gauche
        self.map = PhotoImage(file="cartegood.png")
        self.largeur = self.map.width()
        self.hauteur = self.map.height()

        self.zone_image = Canvas(self.frameBL, width=self.largeur, height=self.hauteur, highlightthickness=0)
        self.zone_image.create_image(0, 0, anchor=NW, image=self.map)
        #self.zone_image.grid(row=0, column=0)

        self.buttonMap = Button(self.frameBL, text="Afficher sur la carte", font=("Helvetica", 20), bg=self.color, command=self.position)
        self.buttonMap.grid(row=1, column=0)
        self.buttonOpenMap = Button(self.frameBL, text="Ouvrir la carte", font=("Helvetica", 20), bg=self.color,
                                    command=self.openMap)
        self.buttonOpenMap.grid(row=1, column=1)



        # frame du bas millieu

        self.labDep = Entry(self.frameB, text="Réponse dep", bg=self.color, fg="white", font=("Helvetica", 30))
        self.labDep.grid(row=0, column=0)
        self.buttonDep = Button(self.frameB, text="Afficher le département", font=("Helvetica", 20), bg=self.color, command=self.dep)
        self.buttonDep.grid(row=1, column=0, pady=20)

        self.esp = Label(self.frameB, bg=self.color, fg="white")
        self.esp.grid(row=2, column=0, pady=30)

        self.labHab = Entry(self.frameB, text="Réponse hab", bg=self.color, fg="white", font=("Helvetica", 30))
        self.labHab.grid(row=3, column=0)
        self.buttonHab = Button(self.frameB, text="Afficher le nombre d'habitants", font=("Helvetica", 20), bg=self.color, command=self.hab)
        self.buttonHab.grid(row=4, column=0, pady=20)
        self.oval = self.zone_image.create_oval(0, 0, 0, 0, outline='white')

        self.nom = 0

        frame = HtmlFrame(self.frameBL)

        frame.set_content("<html><head><title></title></head><body>   <p> SALUT </p>	</body></html>")

        frame.grid(row=0, column=0)

        self.load()

        self.root.mainloop()

    def load(self):

        self.zone_image.delete(self.oval)
        self.num = randint(0, 36568)

        if self.scaleDep.get() != 0:
            while (int(self.data[self.num][16]) < self.scale.get()) or (int(self.data[self.num][1]) != self.scaleDep.get()):
                self.num = randint(0, 36207)
        else:
            while int(self.data[self.num][16]) < self.scale.get():
                self.num = randint(0, 36207)

        self.city = self.data[self.num][5]
        self.labCity.configure(text=self.city)
        self.labHab.delete(0, 12)
        self.labDep.delete(0, 25)

        self.oval = self.zone_image.create_oval(0, 0, 0, 0, outline='white')
        #os.system("killall -9 'Google Chrome'")

    def hab(self):
        self.labHab.delete(0, 12)
        self.labHab.insert(0, self.data[self.num][14])


    def dep(self):
        self.labDep.delete(0, 25)


        for i in range(0, 96):
            if self.depList[i][0] == self.data[self.num][1]:
                self.nom = i

        self.txtDep = self.depList[self.nom][1] + ' (' + self.data[self.num][1] + ')'
        self.labDep.insert(0, self.txtDep)


    def position(self):
        self.zone_image.delete(self.oval)
        self.coordx = (float(self.data[self.num][19])+4.4744) / 0.0295206422 + 104
        self.coordy = (51.0521-float(self.data[self.num][20])) / 0.02035931034 + 59
        self.coordx = round(self.coordx)
        self.coordy = round(self.coordy)
        self.oval = self.zone_image.create_oval(self.coordx-10, self.coordy-10, self.coordx+10, self.coordy+10, outline='red')

    def openMap(self):
        coords = (self.data[self.num][20], self.data[self.num][19])

        map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=6)
        folium.Marker(location=coords, popup=self.city).add_to(map)
        map.save(outfile='map.html')
        webbrowser.open_new('http://localhost:63342/QuizVilles/map.html')



if __name__ == '__main__':
    from tkinter import *
    import csv
    from random import randint
    import folium
    import webbrowser
    import os
    from tkinterhtml import HtmlFrame
    f = App()
