from tkinter import *
from tkinter.messagebox import *
from tkinter import _setit
import string
import random
import tkinter.ttk
from datetime import date

def save_guest():
    #add if statements to disable corresponding checkboxes
    global age_type, final_age
    age=[]
    first_name1 = fname1_var.get()
    last_name1 = lname1_var.ge5t()
    age1 = age1_var.get()
    first_name2 = fname2_var.get()
    last_name2 = lname2_var.get()
    age2 = age2_var.get()
    first_name3 = fname3_var.get()
    last_name3 = lname3_var.get()
    age3 = age3_var.get()

    age.append(age1)
    age.append(age2)
    age.append(age3)

    if bool(first_name1) == True:
        full_name1 = first_name1 + " " + last_name1

        customer_list.append(full_name1)
        customer_age_category.append(age1)

    if bool(first_name2) == True:
        full_name2 = first_name2 + " " + last_name2

        customer_list.append(full_name2)
        customer_age_category.append(age2)

    if bool(first_name3) == True:
        full_name3 = first_name3 + " " + last_name3

        customer_list.append(full_name3)
        customer_age_category.append(age3)

    #print(customer_list)
    #print(customer_age_category)
    save_button.config(state=DISABLED)
    add_guest_button.config(state=DISABLED)
    activity_frame.grid(row=2, column=2, rowspan=2, sticky=W, padx=50, pady=50,ipadx=10)

    final_age = detect_age(age)
    chosen_age_var.set(f'Selected Activity Type: {final_age}')
    detect_activities()
    
def detect_age(age):
    #print(age)
    a = False
    c = False
    
    for i in age:
        if i == "adult":
            a = True
        elif i == "child":
            #print("AAA")
            c = True

    print(a)
    print(c)
    if a == True and c == True:
        return("Family")
        
    elif a == True and c == False:
        return("Adult")

    else:
        return("Child")

    
def detect_activities():
    global final_age

    #print(final_age)
    if final_age == "Adult":
        yoga_check.grid(sticky=W, columnspan=2)
        wine_tasting_check.grid(sticky=W, columnspan=2)
        scubadiving_check.grid(sticky=W, columnspan=2)
        
    elif final_age == "Child":
        mini_golf_check.grid(sticky=W, columnspan=2)
        rock_climbing_check.grid(sticky=W, columnspan=2)
        rope_course_check.grid(sticky=W, columnspan=2)
    
    else:
        hike_check.grid(sticky=W, columnspan=2)
        bike_check.grid(sticky=W, columnspan=2)
        museam_tour_check.grid(sticky=W, columnspan=2)

    activity_count_label.grid(sticky=W)
    activity_count_scale.grid(sticky=W)
    
def add_guest():
    global guest_num
    #guest_num += 1

    print(guest_num)
    
    if guest_num ==1:
        guest2_frame.grid(row=3, column=1, sticky=W, padx=10, pady=10)
        guest_num += 1

    elif guest_num == 2:
        guest3_frame.grid(row=4, column=1, sticky=W, padx=10, pady=10)
        guest_num += 1
        
    elif guest_num >=3:
        showinfo("Message","The max number of guests entered is 3")

    
def register_actvity():
    global customer_services_list, customer_date_list, guest_num, \
           yoga_count, wine_tasting_count, scubadiving_count, bike_count, hike_count, museam_tour_count, mini_golf_count, rock_climbing_count, rope_course_count

    list1 = []
    list2 = []

    list1.append(yoga_var.get())
    list1.append(wine_tasting_var.get())
    list1.append(scubadiving_var.get())
    list1.append(bike_var.get())
    list1.append(hike_var.get())
    list1.append(museam_tour_var.get())
    list1.append(mini_golf_var.get())
    list1.append(rock_climbing_var.get())
    list1.append(rope_course_var.get())
    
    for act in list1:
        if bool(act) == True:
            list2.append(act)

    if bool(yoga_var.get()) == True:
        yoga_count += guest_num
    if bool(wine_tasting_var.get()) == True:
        wine_tasting_count += guest_num
    if bool(scubadiving_var.get()) == True:
        scubadiving_count += guest_num
    if bool(bike_var.get()) == True:
        bike_count += guest_num
    if bool(hike_var.get()) == True:
        hike_count += guest_num
    if bool(museam_tour_var.get()) == True:
        museam_tour_count += guest_num
    if bool(mini_golf_var.get()) == True:
        mini_golf_count += guest_num
    if bool(rock_climbing_var.get()) == True:
        rock_climbing_count += guest_num
    if bool(rope_course_var.get()) == True:
        rope_course_count += guest_num

    #print(yoga_count)
    #print(wine_tasting_count)
            
##    chosen_act = activity_var.get()
    chosen_date = date_var.get()
    #print(chosen_date)
##    
##    listt.append(chosen_act)
    #print(guest_num)
    
    if guest_num == 1:
        customer_services_list.append(list2)
        customer_date_list.append(chosen_date)

        
    elif guest_num == 2:
        customer_services_list.append(list2)
        customer_services_list.append(list2)
        customer_date_list.append(chosen_date)
        customer_date_list.append(chosen_date)

    else:
        customer_services_list.append(list2)
        customer_services_list.append(list2)
        customer_services_list.append(list2)
        customer_date_list.append(chosen_date)
        customer_date_list.append(chosen_date)
        customer_date_list.append(chosen_date)

    
    print(customer_list)
    print(customer_age_category)
    print(customer_services_list)
    print(customer_date_list)
    count_list = [yoga_count, wine_tasting_count, scubadiving_count, bike_count, hike_count, museam_tour_count, mini_golf_count, rock_climbing_count, rope_course_count]
    check_list = [yoga_check, wine_tasting_check, scubadiving_check, bike_check, hike_check, museam_tour_check, mini_golf_check, rock_climbing_check, rope_course_check]


    for i in range (0, len(count_list)):
        count = count_list[i]
        check = check_list[i]
        #print(count)
        if count >= 5:
            #print("aa")
            #index = count_list.index(count)
            check.config(state=DISABLED)

    activity_frame.grid_forget()
    save_button.config(state=NORMAL)
    add_guest_button.config(state=NORMAL)
    
    yoga_check.grid_forget()
    wine_tasting_check.grid_forget()
    scubadiving_check.grid_forget()
    hike_check.grid_forget()
    bike_check.grid_forget()
    museam_tour_check.grid_forget()
    mini_golf_check.grid_forget()
    rock_climbing_check.grid_forget()
    rope_course_check.grid_forget()
    activity_count_label.grid_forget()
    activity_count_scale.grid_forget()
    
    yoga_var.set("")
    wine_tasting_var.set("")
    scubadiving_var.set("")
    hike_var.set("")
    bike_var.set("")
    museam_tour_var.set("")
    mini_golf_var.set("")
    rock_climbing_var.set("")
    rope_course_var.set("")

    guest2_frame.grid_forget()
    guest3_frame.grid_forget()
    
    fname1_var.set("")
    lname1_var.set("")
    age1_var.set("")
    fname2_var.set("")
    lname2_var.set("")
    age2_var.set("")
    fname3_var.set("")
    lname3_var.set("")
    age3_var.set("")

    activity_count_scale.config(troughcolor="#e6e6e6")

    guest_num = 1
    activity_count.set(0)

    year = date.today().year
    month = date.today().month
    day = date.today().day

    date_var.set(f'Today ({year}-{month}-{day})')


    #print("Today's date:", year, month, day)


    
def check_activity():
    list1 = []
    count = 0
    list2 = []
    
    list1.append(yoga_var.get())
    list1.append(wine_tasting_var.get())
    list1.append(scubadiving_var.get())
    list1.append(bike_var.get())
    list1.append(hike_var.get())
    list1.append(museam_tour_var.get())
    list1.append(mini_golf_var.get())
    list1.append(rock_climbing_var.get())
    list1.append(rope_course_var.get())
    print
    for act in list1:
        if bool(act) == True:
            count+=1
    #print(count)
    if count == 3:
        showinfo("Message","Please pick a maximum of 2 activities")

    else:
        register_actvity()

##give initial count
def yoga_countt():
    global yoga_count
    #print(yoga_count)

    if yoga_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif yoga_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(yoga_count)

    #print("AAAA")

    
    
def wine_tasting_countt():
    global wine_tasting_count

    if wine_tasting_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif wine_tasting_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(wine_tasting_count)
    
def scubadiving_countt():
    global scubadiving_count
    if scubadiving_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif scubadiving_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(scubadiving_count)
        
def bike_countt():
    global bike_count
    if bike_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif bike_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(bike_count)
        
def hike_countt():
    global hike_count

    if hike_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif hike_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
 
    activity_count.set(hike_count)
    
def museam_tour_countt():
    global museam_tour_count

    if museam_tour_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif museam_tour_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(museam_tour_count)
    
def mini_golf_countt():
    global mini_golf_count

    if mini_golf_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif mini_golf_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(mini_golf_count)
    
def rock_climbing_countt():
    global rock_climbing_count

    if rock_climbing_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif rock_climbing_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(rock_climbing_count)
    
def rope_course_countt():
    global rope_course_count

    if rope_course_count <= 1:
        activity_count_scale.config(troughcolor="#00FF00")

    elif rope_course_count <=3:
        activity_count_scale.config(troughcolor="#FFFF00")

    else:
        activity_count_scale.config(troughcolor="#FF0000")
    activity_count.set(rope_course_count)


def display_guest():
    global customer_list, customer_age_category, customer_services_list, customer_date_list

    chosen_index_list = []
    name_list = []
    age_list = []
    date_list = []
    name = ""
    age = ""
    date = ""
    
    chosen = display_guest_var.get()

    for i in range(0, len(customer_services_list)):
        if chosen in customer_services_list[i]:
            chosen_index_list.append(i)

    #print(chosen_index_list)

    for a in chosen_index_list:
        name_list.append(customer_list[a])
        age_list.append(customer_age_category[a])
        date_list.append(customer_date_list[a])

    #print(name_list)
    #print(age_list)
    #print(date_list)

    for b in name_list:
        name += f'\n{b}'

    for c in age_list:
        age += f'\n{c}'

    for d in date_list:
        date += f'\n{d}'

    if bool(name_list) == False:
        name += "\nNone"
        age += "\nNone"
        date += "\nNone"
        
    #print(name)
    #print(age)
    #print(date)
    
    name_var.set(f'Name:{name}')
    age_var.set(f'Age:{age}')
    datee_var.set(f'Date:{date}')
    #root.update()
        

def search_guest():
    global list_of_index

    searched = guest_entry_var.get()
    guests = ""
    spin_values = []
    
    for i in range(0, len(customer_list)):
        if searched in customer_list[i]:
            list_of_index.append(i)            


    for a in range(0, len(list_of_index)):
        index = list_of_index[a]
        #print(index)
        guests += f'\n{a+1}. {customer_list[index]}'
        spin_values.append(a+1)

    if bool(guests) == False:
        guests += "\nNone"
    else:
        guest_result_spin.config(values = spin_values)
        guest_result_confirm_button.config(state=NORMAL)
        
    #print(spin_values)
    # print(list_of_index)
        
    guest_result_var.set(f'Guest Results: {guests}')
    result_var.set("")


def show_activities_based_on_guest():
    global list_of_index, customer_services_list, customer_list
    result = ""
    index = guest_result_spin_var.get()

    chosen_index = list_of_index[index-1]
    chosen_activities = customer_services_list[chosen_index]

    for activity in chosen_activities:
        result += f'\n{activity}'
        
    if bool(result) == False:
        result += "None"
        
    result_var.set(f'Chosen Guest: {customer_list[chosen_index]}\nGuest Chosen Activities: {result}')
    list_of_index = []
    guest_result_confirm_button.config(state=DISABLED)
    
    guest_entry_var.set("")
    guest_result_spin_var.set("")
    guest_result_var.set("")
    
def find_customers_by_activity(activity):
    global customer_list, customer_services_list, customer_date_list

    participating_customers = []

    for index in range(0, len(customer_services_list)):
        current_cust_activities = customer_services_list[index]

        if activity in current_cust_activities:
            current_cust = customer_list[index]
            participating_customers.append(current_cust)

    return participating_customers
            

   

#MAIN
global customer_list, customer_age_category, customer_date_list, customer_services_list, guest_num, final_age, list_of_index, \
       yoga_count, wine_tasting_count, scubadiving_count, bike_count, hike_count, museam_tour_count, mini_golf_count, rock_climbing_count, rope_course_count


customer_list = ['Sidrah Haines', 'Hebe Diaz', 'Griff Willis', 'Aamna Levy']
customer_age_category = ['adult', 'adult', 'child', 'child']
customer_services_list = [['yoga', 'wine tasting'], \
                          ['yoga', 'wine tasting'], \
                          [], \
                          ['mini golf', 'rock climbing']]
year = date.today().year
month = date.today().month
day = date.today().day
customer_date_list = [f'Tomorrow ({year}-{month}-{day+1})', f'Today ({year}-{month}-{day})', f'Today ({year}-{month}-{day})', f'Tomorrow ({year}-{month}-{day+1})']
guest_num = 1
list_of_index = []

yoga_count = 2
wine_tasting_count = 2
scubadiving_count = 0
bike_count = 0
hike_count = 0
museam_tour_count = 0
mini_golf_count = 1
rock_climbing_count = 1
rope_course_count = 0


root = Tk()
mainframe = Frame(root)
#create widgets
#do font + color
##**guest registration**
registration_label = Label(mainframe, text="Registration", font=('Marker Felt',60))

guest_frame = LabelFrame(mainframe, text="Enter Guest Information", font=('Marker Felt',30), width=250)

guest1_frame = LabelFrame(guest_frame, text="Guest 1", font=('Marker Felt',20))

fname1_label = Label(guest1_frame, text="First Name", font=('Futura',15))
fname1_var = StringVar()
fname1_entry = Entry(guest1_frame, width=20, textvariable=fname1_var, font=('Futura',12))

lname1_label = Label(guest1_frame, text="Last Name", font=('Futura',15))
lname1_var = StringVar()
lname1_entry = Entry(guest1_frame, width=20, textvariable=lname1_var, font=('Futura',12))

age1_label = Label(guest1_frame, text="Age Category", font=('Futura',15))
age_categories = [ 'child', 'adult'] 
age1_var = StringVar()
age1_spin = Spinbox(guest1_frame, textvariable=age1_var, values=age_categories, font=('Futura',12))
age1_var.set("")

guest2_frame = LabelFrame(guest_frame, text="Guest 2", font=('Marker Felt',20))

fname2_label = Label(guest2_frame, text="First Name", font=('Futura',15))
fname2_var = StringVar()
fname2_entry = Entry(guest2_frame, width=20, textvariable=fname2_var, font=('Futura',12))

lname2_label = Label(guest2_frame, text="Last Name", font=('Futura',15))
lname2_var = StringVar()
lname2_entry = Entry(guest2_frame, width=20, textvariable=lname2_var, font=('Futura',12))

age2_label = Label(guest2_frame, text="Age Category", font=('Futura',15))
age_categories = [ 'child', 'adult'] 
age2_var = StringVar()
age2_spin = Spinbox(guest2_frame, textvariable=age2_var, font=('Futura',12), values=age_categories)
age2_var.set("")

guest3_frame = LabelFrame(guest_frame, text="Guest 3", font=('Marker Felt',20))

fname3_label = Label(guest3_frame, text="First Name", font=('Futura',15))
fname3_var = StringVar()
fname3_entry = Entry(guest3_frame, width=20, textvariable=fname3_var, font=('Futura',12))

lname3_label = Label(guest3_frame, text="Last Name", font=('Futura',15))
lname3_var = StringVar()
lname3_entry = Entry(guest3_frame, width=20, textvariable=lname3_var, font=('Futura',12))

age3_label = Label(guest3_frame, text="Age Category", font=('Futura',15))
age_categories = ['child', 'adult'] 
age3_var = StringVar()
age3_spin = Spinbox(guest3_frame, textvariable=age3_var, values=age_categories, font=('Futura',12))
age3_var.set("")

add_guest_button = Button(guest_frame, text="Add Another Guest", command=add_guest, font=('Futura',12), fg="#0000FF")

save_button = Button(guest_frame, text="SAVE", command=save_guest, font=('Futura',12), fg="#0000FF")

##activity registration
activity_frame = LabelFrame(mainframe, text="Activity Registration", font=('Marker Felt',30))

chosen_age_var = StringVar()
chosen_age_var.set("Selected Activity Type:")
chosen_age_label = Label(activity_frame, textvariable=chosen_age_var, font=('Futura',15))

date_label = Label(activity_frame, text="Pick a Date", font=('Futura',15))

date_var = StringVar()
date_var.set(f'Today ({year}-{month}-{day})')
today_radio = Radiobutton(activity_frame, text=f'Today ({year}-{month}-{day})', variable=date_var, font=('Futura',15), value=f'Today ({year}-{month}-{day})')
tomorrow_radio = Radiobutton(activity_frame, text=f'Tomorrow ({year}-{month}-{day+1})', variable=date_var, font=('Futura',15), value=f'Tomorrow ({year}-{month}-{day+1})')
day_after_radio = Radiobutton(activity_frame, text=f'{year}-{month}-{day+2}', variable=date_var, font=('Futura',15), value=f'{year}-{month}-{day+2}')

##date_list = [f'Today ({year}-{month}-{day})',f'Tomorrow ({year}-{month}-{day+1})', f'{year}-{month}-{day+2}']
##date_var.set(f'Today ({year}-{month}-{day})')
##date_option = OptionMenu(activity_frame, date_var, *date_list)
##date_option.config(font=('Futura',15), width=17)

choose_activity_frame = LabelFrame(activity_frame, text="Acitivities", font=('Marker Felt',20))

yoga_var = StringVar()
yoga_check = Checkbutton(choose_activity_frame, text="Yoga", variable=yoga_var, onvalue="yoga", offvalue="", command=yoga_countt, font=('Futura',15))

wine_tasting_var = StringVar()
wine_tasting_check = Checkbutton(choose_activity_frame, text="Wine Tasting", variable=wine_tasting_var, onvalue="wine tasting", offvalue="", command=wine_tasting_countt, font=('Futura',15))

scubadiving_var = StringVar()
scubadiving_check = Checkbutton(choose_activity_frame, text="Scubadiving", variable=scubadiving_var, onvalue="scubadiving", offvalue="", command=scubadiving_countt, font=('Futura',15))

bike_var = StringVar()
bike_check = Checkbutton(choose_activity_frame, text="Bike", variable=bike_var, onvalue="bike", offvalue="", command=bike_countt, font=('Futura',15))

hike_var = StringVar()
hike_check = Checkbutton(choose_activity_frame, text="Hike", variable=hike_var, onvalue="hike", offvalue="", command=hike_countt, font=('Futura',15))

museam_tour_var = StringVar()
museam_tour_check = Checkbutton(choose_activity_frame, text="Museam Tour", variable=museam_tour_var, onvalue="museam tour", offvalue="", command=museam_tour_countt, font=('Futura',15))

mini_golf_var = StringVar()
mini_golf_check = Checkbutton(choose_activity_frame, text="Mini Golf", variable=mini_golf_var, onvalue="mini golf", offvalue="", command=mini_golf_countt, font=('Futura',15))

rock_climbing_var = StringVar()
rock_climbing_check = Checkbutton(choose_activity_frame, text="Rock Climbing", variable=rock_climbing_var, onvalue="rock climbing", offvalue="", command=rock_climbing_countt, font=('Futura',15))

rope_course_var = StringVar()
rope_course_check = Checkbutton(choose_activity_frame, text="Rope Course", variable=rope_course_var, onvalue="rope course", offvalue="", command=rope_course_countt, font=('Futura',15))

activity_save_button = Button(activity_frame, text="SAVE", command=check_activity, font=('Futura',15), fg="#0000FF")

activity_count_label = Label(choose_activity_frame, text="# of People signed:", font=('Futura',12))

activity_count = StringVar()
activity_count.set(0)
activity_count_scale = Scale(choose_activity_frame, state=DISABLED, from_=0, to=5, variable=activity_count, orient=HORIZONTAL, showvalue=True, font=('Futura',12))

##display guests base don activities
display_guest_frame = LabelFrame(mainframe, text="Display guests based on activity", font=('Marker Felt',30))

display_guest_var = StringVar()
display_guest_var.set("")
display_guest_list = ["yoga", "wine tasting", "scubadiving", "bike", "hike", "museam tour", "mini golf", "rock climbing", "rope course"]
display_guest_option = OptionMenu(display_guest_frame, display_guest_var, *display_guest_list)
display_guest_option.config(width=10, font=('Futura',12))

display_guest_button = Button(display_guest_frame, text="Display", font=('Futura',12), command=display_guest, fg="#0000FF")

display_guest_label = Label(display_guest_frame, text="List of Guests")

name_var = StringVar()
name_var.set("Name")
name_label = Label(display_guest_frame, textvariable=name_var, width=20, font=('Futura',12))

age_var = StringVar()
age_var.set("Age")
age_label = Label(display_guest_frame, textvariable=age_var, width=5, font=('Futura',12))

datee_var = StringVar()
datee_var.set("Date")
datee_label = Label(display_guest_frame, textvariable=datee_var, width=20, font=('Futura',12))

##display activities based on guest
display_activities_frame = LabelFrame(mainframe, text="Display activities based on guest", font=('Marker Felt',30), height=500)

enter_guest_label = Label(display_activities_frame, text="Enter Guest Name", font=('Futura',15))

guest_entry_var = StringVar()
guest_entry = Entry(display_activities_frame, textvariable=guest_entry_var, font=('Futura',12))

guest_seatch_button = Button(display_activities_frame, text="Search", fg="#0000FF", font=('Futura',12), command=search_guest)

guest_result_var = StringVar()
guest_result_var.set("Guest Results:")
guest_result_label = Label(display_activities_frame, font=('Futura',15), textvariable=guest_result_var)

guest_result_spin_var = IntVar()
guest_result_spin_list = []
guest_result_spin_label = Label(display_activities_frame, font=('Futura',15), text="Select the guest's list #")
guest_result_spin = Spinbox(display_activities_frame, textvariable=guest_result_spin_var, values=guest_result_spin_list)
guest_result_spin.config(font=('Futura',12))
    
guest_result_confirm_button = Button(display_activities_frame, fg="#0000FF", state=DISABLED, font=('Futura',12), text="confirm", command=show_activities_based_on_guest)


result_var = StringVar()
result_var.set("")
result_label = Label(display_activities_frame, font=('Futura',18), textvariable=result_var)

#grid widgets
mainframe.grid(padx=50, pady=50)

registration_label.grid(row=1, column=1, columnspan=2)
guest_frame.grid(row=2, column=1, padx=30, pady=30, sticky=EW, rowspan=2)

guest1_frame.grid(row=1, column=1, sticky=W, padx=10, pady=10)

fname1_label.grid(row=1, column=1, sticky=W)
fname1_entry.grid(row=1, column=2, sticky=W, padx=10)
lname1_label.grid(row=2, column=1, sticky=W)
lname1_entry.grid(row=2, column=2, sticky=W, padx=10)
age1_label.grid(row=3, column=1, sticky=W)
age1_spin.grid(row=3, column=2, sticky=W, padx=10)
add_guest_button.grid(row=4, column=1)
save_button.grid(row=5, column=1)

fname2_label.grid(row=1, column=1)
fname2_entry.grid(row=1, column=2)
lname2_label.grid(row=2, column=1)
lname2_entry.grid(row=2, column=2)
age2_label.grid(row=3, column=1)
age2_spin.grid(row=3, column=2)

fname3_label.grid(row=1, column=1)
fname3_entry.grid(row=1, column=2)
lname3_label.grid(row=2, column=1)
lname3_entry.grid(row=2, column=2)
age3_label.grid(row=3, column=1)
age3_spin.grid(row=3, column=2)

add_guest_button.grid(row=5, column=1)
save_button.grid(row=6, column=1)

##choose activity

chosen_age_label.grid(row=1, column=1, sticky=W, columnspan=2, padx=10)

date_label.grid(row=2, column=1, sticky=W, padx=10)
today_radio.grid(row=2, column=2, sticky=W)
tomorrow_radio.grid(row=3, column=2, sticky=W)
day_after_radio.grid(row=4, column=2, sticky=W)

choose_activity_frame.grid(row=5, column=1, sticky=W, columnspan=2, pady=10, padx=10, ipadx=10, ipady=10)
##yoga_radio.grid(sticky=W)
##wine_tasting_radio.grid(sticky=W)
##scubadiving_radio.grid(sticky=W)
##hike_radio.grid(sticky=W)
##bike_radio.grid(sticky=W)
##museam_tour_radio.grid(sticky=W)
##mini_golf_radio.grid(sticky=W)
##rock_climbing_radio.grid(sticky=W)
##rope_course_radio.grid(sticky=W)

activity_save_button.grid(row=6, column=1, columnspan=2)

##display guests based on activities
display_guest_frame.grid(row=2, column=3, ipadx=10, ipady=10, padx=30, pady=30)

display_guest_option.grid(row=1, column=1, columnspan=4, pady=10)
display_guest_button.grid(row=2, column=1, columnspan=3)
name_label.grid(row=3, column=1, sticky=W)
age_label.grid(row=3, column=2, sticky=W)
datee_label.grid(row=3, column=3, sticky=W)

##display activities based on guest
display_activities_frame.grid(row=3, column=3, padx=30, pady=30)

enter_guest_label.grid(row=1, column=1, padx=10, pady=10)
guest_entry.grid(row=1, column=2, pady=10)
guest_seatch_button.grid(row=2, column=1, columnspan=3)

guest_result_label.grid(row=3, column=1, pady=10, sticky=N)
guest_result_spin_label.grid(row=3, column=2, sticky=N)
guest_result_spin.grid(row=4, column=2, pady=10, sticky=N)
guest_result_confirm_button.grid(row=4, column=3, pady=10, sticky=N)

result_label.grid(row=5, column=1, columnspan=3, rowspan=2)


root.mainloop()

#FOR TESTING PURPOSES

search_activity = input('Enter activity name')
participating_cust = find_customers_by_activity(search_activity)
#print(participating_cust)
