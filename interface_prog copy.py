from tkinter import *

list_var = ["крестики","нолики"]
prize_variant = [['(0,0)','(0,1)','(0,2)'],['(0,2)','(1,2)','(2,2)'],['(2,2)','(2,1)','(2,0)'],['(2,0)','(1,0)','(0,0)'],
                 ['(0,1)','(1,1)','(2,1)'],['(0,0)','(1,1)','(2,2)'],['(2,0)','(1,1)','(0,2)']]



class Player:
    
    def __init__(self, name, figure, image) -> None:
        self.game_status = False
        self.name = name
        self.image = image
        self.list_push = []
        self.figure = figure

    def __str__(self) -> str:
        return f"{self.name} играет за {self.figure} cтатус активного хода : {self.game_status} "
    
    def check_result(self):
        
        for variant in prize_variant:
            print(variant)
            count = 0
            for i in variant:
                if i in self.list_push:
                    count+=1
                    print(f' в проверяемой строке {variant} у игрока {self.name} {count} совпадений')
                    if count==3: 
                        print("выигрыш")
                        return f'выиграл {self.name}'
                    
        return ""        
        



def click_change(event):
    text = button["text"]
    button["text"] = "Это ваш выбор?"

def noclick_change(event):
    button["text"] = "Не нажата"


def entry_label(header_entry_label):
    result_frame = Frame()
    lab_frame = Label(result_frame, text=f"{header_entry_label}")
    lab_frame.pack(side=TOP, fill=BOTH, expand=1)
    entry_frame = Entry(result_frame)
    entry_frame.pack(fill=BOTH, expand=1)
    return [result_frame, entry_frame]

def choose_variant(name_frame):
    list_variant = StringVar(value=list_var)
    ls_box = Listbox(name_frame, listvariable=list_variant, height=3)
    return ls_box
ls = [0,1]    
def return_choose(event):
    global list_var
    figure_2_player = ""
    
    dict_name_and_figure = dict()
    name1= first_player_frame[1].get()
    name2= second_player_frame[1].get()
    index1 = list(ls_name1.curselection())
    index1_int = index1[0]
    figure_1_player = ls_name1.get(first=index1_int)
    
    first = list_var[0]
    second = list_var[1]
    if figure_1_player == first: 
        figure_2_player = second
    else: figure_2_player = first
    first_player = Player(name1, figure_1_player, cross)
    second_player = Player(name2, figure_2_player, zero)
    
    res_status = get_game_status(first_player, second_player)

    valentin = res_status[0]
    leonid = res_status[1]

    

    second_name_lab["text"] = leonid.name
    first_name_lab["text"] = valentin.name
    if valentin.name == "крестики":
        first_figure_lab.config(image=cross, text = "")
        second_figure_lab.config(image=zero, text = "")
        view_status_player_lab.configure(text=f'{valentin.name}', fg="green", font=("Arial", 16))
    else:
        first_figure_lab.config(image=zero, text = "")
        second_figure_lab.config(image=cross, text = "")
        view_status_player_lab.configure(text=f'{leonid.name}', fg="green", font=("Arial", 16))
    #first_figure_lab["text"] = f'играет за {valentin.figure}'
    #second_figure_lab["text"] = f'играет за {leonid.figure}'
   #ls2 = set(ls).difference(list(index1_int))
    #ls_name2.select_set(first=index1_int)
    print(valentin, leonid)
    
    result_game = game_round(first_player, second_player, gaming_field)
    
    return first_player, second_player
    
    
#def press(x):
#    x["text"] = "нажата"

def get_game_status(player1, player2):
    if player1.figure == "крестики":
        player1.game_status = True
        player2.game_status = False
    else:
        player1.game_status = False
        player2.game_status = True 
    return player2, player1       

def step_game(first_pl, second_pl, butt):
    if first_pl.game_status == True:
        view_status_player_lab["text"] = f'{first_pl.name}'
        print(f"ходит игрок с именем {first_pl.name} ")
        change_step = butt["text"]
        butt.configure(image=first_pl.image, text='', state=DISABLED)
        first_pl.list_push.append(change_step)
        first_pl.game_status = False
        second_pl.game_status = True
        print(f'с начала игры {first_pl.name} нажал кнопки {first_pl.list_push}')
        push_first_player = first_pl.list_push
        result_check = first_pl.check_result()
        if result_check:
            print(result_check)
            view_status_player_lab["text"] = f'{result_check}'
        view_status_player_lab["text"] = f'{second_pl.name}'
        #print(f"после нажатия статут хода {first_pl.game_status} ")
        
    elif second_pl.game_status == True:
        view_status_player_lab["text"] = f'{second_pl.name}'
        print(f"ходит игрок с именем {second_pl.name} ")
        change_step = butt["text"]
        butt.configure(image=second_pl.image, text='', state=DISABLED)
        second_pl.list_push.append(change_step)
        print(f'с начала игры {second_pl.name} нажал кнопки {second_pl.list_push}')
        result_check = second_pl.check_result()
        if result_check:
            print(result_check)
            view_status_player_lab["text"] = f'{result_check}'
        view_status_player_lab["text"] = f'ходит игорок с именем {first_pl.name}'
        second_pl.game_status = False
        first_pl.game_status = True

def game_round(first_gamer, second_gamer, play_field):
    print("ну что поиграем!!!!!!!!!!!!")
    for button in play_field:
        x = button[0]
        x.configure(command = lambda item=x: step_game(first_gamer, second_gamer, item))
        
    #return first_gamer.list_push, second_gamer.list_push


root = Tk()
root.title("Крестики-нолики!!!")
root.geometry("600x800")

cross = PhotoImage(file="./cross.png")
zero = PhotoImage(file="./zero.png")

for i in range(3): root.columnconfigure( index = i, weight=1)
for i in range(7): root.rowconfigure( index = i, weight=1)

invitation_lab = Label(text="Приглашаем Вас сыграть в крестики-нолики!!!")
invitation_lab.grid(column=0,row=0, columnspan=3)

first_player_frame = entry_label("Имя первого игрока:")

first_player_frame[0].grid(row = 1, column= 0, columnspan=2)
second_player_frame = entry_label("Имя второго игрока:")
second_player_frame[0].grid(row = 2, column = 0, columnspan=2)

ls_name1 = choose_variant(first_player_frame[0])
ls_name1.pack()

ls_name2 = choose_variant(second_player_frame[0])
ls_name2.pack()

demonstrate_game_frame = LabelFrame(text='отображение хода игры')
demo_first_player = Frame(demonstrate_game_frame)
first_name_lab = Label(demo_first_player, text="Первый игрок")
first_figure_lab = Label(demo_first_player, text="Изображение")
first_name_lab.pack()
first_figure_lab.pack()
demo_first_player.pack(side=LEFT)

demo_second_player = Frame(demonstrate_game_frame)
second_name_lab = Label(demo_second_player, text="Второй игрок")
second_figure_lab = Label(demo_second_player, text="Изображение")
second_name_lab.pack()
second_figure_lab.pack()
demo_second_player.pack(side=LEFT)

view_status_player_lab = Label(demonstrate_game_frame, text="Здесь отображается имя активного игрока", wraplength=150)
view_status_player_lab.pack(anchor=S)

demonstrate_game_frame.grid(column = 2, row = 1, rowspan=2)






gaming_field = list()

for row in range(4,7):
    for column in range(3):
        button = Button(text=f"({row-4},{column})")
        #button.bind("<Enter>", click_change)
        #button.bind("<Leave>", noclick_change)
        #button.configure(command= press)
        button.grid(row = row, column= column, sticky=NSEW)
        gaming_field.append((button, row, column))
        

#gaming_field[0][0].bind("<Enter>", click_change)
#gaming_field[0][0].bind("<Leave>", noclick_change)

#for button in gaming_field:
#    item = button[0]
#    item.configure(command = lambda x = item: press(x))

    

ls_name1.bind("<<ListboxSelect>>", return_choose)


# valentin = Player("Валентин", "крестики", cross)
# valentin.game_status = True
# leonid = Player("Леонид", "нолики", zero)
# leonid.game_status = False



#start_game_button = Button(text="Начать игру", command= start_game)
#quantity_motiones_lab = Label(quantity_motiones_frame, text="")
#quantity_motiones_lab.pack(fill=BOTH, expand=1)
#start_game_button.grid(column = 0, row = 3, columnspan=2)



root.mainloop()

#if __name__ == "__main__":
 