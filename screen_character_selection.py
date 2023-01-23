import tkinter

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
       # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character_index = tkinter.StringVar()
        self.character_index.set(None)

        #
        # TO DO
        #
        tkinter.Label(self,font = ("Helvetica",20)).grid(row=0,column=0,columnspan=3,sticky=tkinter.N)
        tkinter.Label(self,text = "Hit Points", font = ("Helvetica",20)).grid(row=1,column=2,columnspan=3,sticky=tkinter.N)
        tkinter.Label(self,text = "Dexterity", font = ("Helvetica",20)).grid(row=1,column=3,columnspan=3,sticky=tkinter.N)
        tkinter.Label(self,text = "Strength", font = ("Helvetica",20)).grid(row=1,column=4,columnspan=3,sticky=tkinter.N)

        row_num = 2
        char_num = 0
        for char in self.roster.character_list:
            imageElf = tkinter.PhotoImage(file = "images/"+char.small_image)
            tkinter.Radiobutton(self,text=char.name,variable=self.character,value=char.num,font=("Helvetica",16)).grid(row=row_num,column=0,sticky=tkinter.N)
            self.callback_on_selected(self.character_index.get())
            lbl = tkinter.Label(self,image=imageElf)
            lbl.x = imageElf
            lbl.grid(row=row_num,column=1,sticky=tkinter.W)

            tkinter.Label(self,text=str(char.hit_points),font=("Helvetica",16),width=10).grid(row=row_num,column=2,sticky=tkinter.W)
            tkinter.Label(self,text=str(char.dexterity),font=("Helvetica",16),width=10).grid(row=row_num,column=2,sticky=tkinter.W)
            tkinter.Label(self,text=str(char.strength),font=("Helvetica",16),width=10).grid(row=row_num,column=2,sticky=tkinter.W)
            

            row_num += 1
            char_num += 1
        tkinter.Button(self,text="Character Selection",fg="Red",bg="Black",font=("Helvetica",16)).grid(row=row_num,column=2,columnspan=3,sticky=tkinter.N)

    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
    