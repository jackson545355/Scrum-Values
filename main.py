import turtle
import tkinter as tk
from tkinter import  *

# Nhap du lieu
Commitment = 0
Openness = 0
Respect = 0
Courage = 0
Focus = 0

background_color = "#FFC0CB" # đỏ
foreground_color = "#696969" # trắng

# tao widget
window = tk.Tk()

label_commitment = tk.Label(window, text="Commitment", font=("Helvetica",15))

check_var = tk.IntVar()
check_var_1 = tk.IntVar()
check_var_2 = tk.IntVar()
check_var_3 = tk.IntVar()
check_var_4 = tk.IntVar()
# Tạo checkbox và gán biến IntVar vào thuộc tính "variable" của checkbox
checkbox_0 = tk.Checkbutton(window, text="1. I always know what the sprint goal is and how my work supports it.", variable=check_var,font=("Helvetica",12))
checkbox_1 = tk.Checkbutton(window, text="2. I do everything I can to ensure we achieve the goals of the sprint.", variable=check_var_1,font=("Helvetica",12))
checkbox_2 = tk.Checkbutton(window, text="3. In my current team, I have never thought of taking a sick day to avoid going into work.", variable=check_var_2,font=("Helvetica",12))
checkbox_3 = tk.Checkbutton(window, text="4. I always arrive on time for the events, my colleagues never have to wait for me to start the event.", variable=check_var_3,font=("Helvetica",12))
checkbox_4 = tk.Checkbutton(window, text="5. I know what it means to say that an item is done, i.e. I know the criteria that meets our Definition of Done.", variable=check_var_4,font=("Helvetica",12))

label_commitment.pack(anchor="center")
checkbox_0.pack(anchor="w")
checkbox_1.pack(anchor="w")
checkbox_2.pack(anchor="w")
checkbox_3.pack(anchor="w")
checkbox_4.pack(anchor="w")

label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")


# Hàm xử lý sự kiện khi nhấn nút "Submit"
def submit():
    global Commitment
    if check_var.get() == 1:
        print("Checkbox 1 is checked")
        Commitment+=1
    if check_var_1.get() == 1:
        print("Checkbox 2 is checked")
        Commitment += 1
    if check_var_2.get() == 1:
        print("Checkbox 3 is checked")
        Commitment += 1
    if check_var_3.get() == 1:
        print("Checkbox 4 is checked")
        Commitment += 1
    if check_var_4.get() == 1:
        print("Checkbox 5 is checked")
        Commitment += 1

    print("Commitment bien la : " + str(Commitment))
    window.after(1000, window.destroy)
label_thuthang.pack(anchor="center")

# Tạo nút "Submit" để kiểm tra trạng thái của checkbox
submit_button = tk.Button(window, text="Next", command=submit,font=("Helvetica",11))
submit_button.pack()

# Đặt tiêu đề cho cửa sổ
window.title("Scrum Values")
#window.config(bg=background_color)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Tính toán tọa độ trung tâm của cửa sổ
x = int((screen_width - 770) / 2)
y = int((screen_height - 225) / 2)
window.geometry(f"770x225+{x}+{y}")

#label_Thut hang#label_thuthang1 = tk.Label(window,text="-------------------------------------------------------------------------------")
#label_thuthang2 = tk.Label(window,text="-------------------------------------------------------------------------------")
#label_thuthang3 = tk.Label(window,text="-------------------------------------------------------------------------------")

# Tắt window sau 30 giây
window.after(300000, window.destroy)

# Chạy vòng lặp chính của giao diện
window.mainloop()

#--------------------------------------------------------------------------------

window = tk.Tk()
window.title("Scrum Values")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Tính toán tọa độ trung tâm của cửa sổ
x = int((screen_width - 650) / 2)
y = int((screen_height - 225) / 2)
#window.config(bg=background_color)
window.geometry(f"650x225+{x}+{y}")
label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")
# Tạo một đối tượng nhãn Label để hiển thị thông tin Openness
label_Openness = tk.Label(window, text="Openness", anchor="center", font=("Helvetica",15))
check_var = tk.IntVar()
check_var_1 = tk.IntVar()
check_var_2 = tk.IntVar()
check_var_3 = tk.IntVar()
check_var_4 = tk.IntVar()
# Tạo checkbox và gán biến IntVar vào thuộc tính "variable" của checkbox
checkbox_0 = tk.Checkbutton(window, text="1. I do not shy away from telling difficult news to team members and stakeholders.", variable=check_var,font=("Helvetica",12))
checkbox_1 = tk.Checkbutton(window, text="2. I do not hide away difficult issues in the hope that they will sort themselves out.", variable=check_var_1,font=("Helvetica",12))
checkbox_2 = tk.Checkbutton(window, text="3. If something / someone is annoying me I will address it / tell them.", variable=check_var_2,font=("Helvetica",12))
checkbox_3 = tk.Checkbutton(window, text="4. My colleagues can judge what state of mind I'm in, I can share my feelings with my them.", variable=check_var_3,font=("Helvetica",12))
checkbox_4 = tk.Checkbutton(window, text="5. I always say the true state of an item, and do not over/under play it.", variable=check_var_4,font=("Helvetica",12))

label_Openness.pack(anchor="center")
checkbox_0.pack(anchor="w")
checkbox_1.pack(anchor="w")
checkbox_2.pack(anchor="w")
checkbox_3.pack(anchor="w")
checkbox_4.pack(anchor="w")

label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")


# Hàm xử lý sự kiện khi nhấn nút "Submit"
def submit():
    global Openness
    if check_var.get() == 1:
        print("Checkbox 1 is checked")
        Openness += 1
    if check_var_1.get() == 1:
        print("Checkbox 2 is checked")
        Openness += 1
    if check_var_2.get() == 1:
        print("Checkbox 3 is checked")
        Openness += 1
    if check_var_3.get() == 1:
        print("Checkbox 4 is checked")
        Openness += 1
    if check_var_4.get() == 1:
        print("Checkbox 5 is checked")
        Openness += 1

    print("Openness bien la : " + str(Openness))
    window.after(1000, window.destroy)
label_thuthang.pack(anchor="center")
submit_button = tk.Button(window, text="Next", command=submit,font=("Helvetica",11))
submit_button.pack()
# Tắt window sau 30 giây
window.after(300000, window.destroy)

# Chạy vòng lặp chính của giao diện
window.mainloop()

#label_thuthang1.pack(anchor="center")

#--------------------------------------------------------------------------------

window = tk.Tk()
window.title("Scrum Values")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Tính toán tọa độ trung tâm của cửa sổ
x = int((screen_width - 570) / 2)
y = int((screen_height - 225) / 2)
window.geometry(f"570x225+{x}+{y}")
label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")
#window.config(bg=background_color)
# Tạo một đối tượng nhãn Label để hiển thị thông tin Respect
label_Respect = tk.Label(window, text="Respect", anchor="center", font=("Helvetica",15))
check_var = tk.IntVar()
check_var_1 = tk.IntVar()
check_var_2 = tk.IntVar()
check_var_3 = tk.IntVar()
check_var_4 = tk.IntVar()
# Tạo checkbox và gán biến IntVar vào thuộc tính "variable" của checkbox
checkbox_0 = tk.Checkbutton(window, text="1. I listen with equal intensity regardless of who is talking.", variable=check_var,font=("Helvetica",12))
checkbox_1 = tk.Checkbutton(window, text="2. When listening to people I never talk over them.", variable=check_var_1,font=("Helvetica",12))
checkbox_2 = tk.Checkbutton(window, text="3. I value everyone's opinion equally.", variable=check_var_2,font=("Helvetica",12))
checkbox_3 = tk.Checkbutton(window, text="4. I am never concerned who works on what item in the backlog.", variable=check_var_3,font=("Helvetica",12))
checkbox_4 = tk.Checkbutton(window, text="5. I feel that my opinion is respected and that I have an equal say in the team.", variable=check_var_4,font=("Helvetica",12))

label_Respect.pack(anchor="center")
checkbox_0.pack(anchor="w")
checkbox_1.pack(anchor="w")
checkbox_2.pack(anchor="w")
checkbox_3.pack(anchor="w")
checkbox_4.pack(anchor="w")

label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")


# Hàm xử lý sự kiện khi nhấn nút "Submit"
def submit():
    global Respect
    if check_var.get() == 1:
        print("Checkbox 1 is checked")
        Respect += 1
    if check_var_1.get() == 1:
        print("Checkbox 2 is checked")
        Respect += 1
    if check_var_2.get() == 1:
        print("Checkbox 3 is checked")
        Respect += 1
    if check_var_3.get() == 1:
        print("Checkbox 4 is checked")
        Respect += 1
    if check_var_4.get() == 1:
        print("Checkbox 5 is checked")
        Respect += 1

    print("Respect bien la : " + str(Respect))
    window.after(1000, window.destroy)
label_thuthang.pack(anchor="center")
submit_button = tk.Button(window, text="Next", command=submit,font=("Helvetica",11))
submit_button.pack()
# Tắt window sau 30 giây
window.after(300000, window.destroy)

# Chạy vòng lặp chính của giao diện
window.mainloop()

#label_thuthang2.pack(anchor="center")
#--------------------------------------------------------------------------------


window = tk.Tk()
window.title("Scrum Values")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Tính toán tọa độ trung tâm của cửa sổ
x = int((screen_width - 790) / 2)
y = int((screen_height - 225) / 2)
window.geometry(f"790x225+{x}+{y}")
label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")
#window.config(bg=background_color)
# Tạo một đối tượng nhãn Label để hiển thị thông tin Courage
label_Courage = tk.Label(window, text="Courage", anchor="center", font=("Helvetica",15))
check_var = tk.IntVar()
check_var_1 = tk.IntVar()
check_var_2 = tk.IntVar()
check_var_3 = tk.IntVar()
check_var_4 = tk.IntVar()
# Tạo checkbox và gán biến IntVar vào thuộc tính "variable" của checkbox
checkbox_0 = tk.Checkbutton(window, text="1. I work on the next highest priority Product Backlog Item (I do not cherry pick the work I pick up in the Sprint).", variable=check_var,font=("Helvetica",12))
checkbox_1 = tk.Checkbutton(window, text="2. If I see something that is wrong with what I'm being asked to do, I will say so.", variable=check_var_1,font=("Helvetica",12))
checkbox_2 = tk.Checkbutton(window, text="3. I will question & reproach my team members if I feel that they are doing something wrong.", variable=check_var_2,font=("Helvetica",12))
checkbox_3 = tk.Checkbutton(window, text="4. Regardless of the person talking, I will correct them if I believe that they are incorrect.", variable=check_var_3,font=("Helvetica",12))
checkbox_4 = tk.Checkbutton(window, text="5. I will stand firm if I believe I am right, even if I'm in the minority within the group.", variable=check_var_4,font=("Helvetica",12))

label_Courage.pack(anchor="center")
checkbox_0.pack(anchor="w")
checkbox_1.pack(anchor="w")
checkbox_2.pack(anchor="w")
checkbox_3.pack(anchor="w")
checkbox_4.pack(anchor="w")

#label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")


# Hàm xử lý sự kiện khi nhấn nút "Submit"
def submit():
    global Courage
    if check_var.get() == 1:
        print("Checkbox 1 is checked")
        Courage += 1
    if check_var_1.get() == 1:
        print("Checkbox 2 is checked")
        Courage += 1
    if check_var_2.get() == 1:
        print("Checkbox 3 is checked")
        Courage += 1
    if check_var_3.get() == 1:
        print("Checkbox 4 is checked")
        Courage += 1
    if check_var_4.get() == 1:
        print("Checkbox 5 is checked")
        Courage += 1

    print("Courage bien la : " + str(Courage))
    window.after(1000, window.destroy)
label_thuthang.pack(anchor="center")
submit_button = tk.Button(window, text="Next", command=submit,font=("Helvetica",11))
submit_button.pack()

# Tắt window sau 30 giây
window.after(300000, window.destroy)

# Chạy vòng lặp chính của giao diện
window.mainloop()
#label_thuthang3.pack(anchor="center")
#--------------------------------------------------------------------------------

window = tk.Tk()
window.title("Scrum Values")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Tính toán tọa độ trung tâm của cửa sổ
x = int((screen_width - 1070) / 2)
y = int((screen_height - 225) / 2)
window.geometry(f"1070x225+{x}+{y}")
label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")
#window.config(bg=background_color)
# Tạo một đối tượng nhãn Label để hiển thị thông tin Focus
label_Focus = tk.Label(window, text="Focus", anchor="center", font=("Helvetica",15))
check_var = tk.IntVar()
check_var_1 = tk.IntVar()
check_var_2 = tk.IntVar()
check_var_3 = tk.IntVar()
check_var_4 = tk.IntVar()
# Tạo checkbox và gán biến IntVar vào thuộc tính "variable" của checkbox
checkbox_0 = tk.Checkbutton(window, text="1. Whilst working on a story I do not get distracted.", variable=check_var,font=("Helvetica",12))
checkbox_1 = tk.Checkbutton(window, text="2. If I am not enjoying the work in a story I still give it the attention it needs.", variable=check_var_1,font=("Helvetica",12))
checkbox_2 = tk.Checkbutton(window, text="3. When enjoying working on a story I will not over work a story just to prolong it.", variable=check_var_2,font=("Helvetica",12))
checkbox_3 = tk.Checkbutton(window, text="4. I do not procrastinate when working on a story.", variable=check_var_3,font=("Helvetica",12))
checkbox_4 = tk.Checkbutton(window, text="5. As soon as the story is ready to move into a new state, I will tell my colleagues and either hand it over or ensure that they know it is ready to pick up.", variable=check_var_4,font=("Helvetica",12))

label_Focus.pack(anchor="center")
checkbox_0.pack(anchor="w")
checkbox_1.pack(anchor="w")
checkbox_2.pack(anchor="w")
checkbox_3.pack(anchor="w")
checkbox_4.pack(anchor="w")

#label_thuthang = tk.Label(window,text="-------------------------------------------------------------------------------")


# Hàm xử lý sự kiện khi nhấn nút "Submit"
def submit():
    global Focus
    if check_var.get() == 1:
        print("Checkbox 1 is checked")
        Focus += 1
    if check_var_1.get() == 1:
        print("Checkbox 2 is checked")
        Focus += 1
    if check_var_2.get() == 1:
        print("Checkbox 3 is checked")
        Focus += 1
    if check_var_3.get() == 1:
        print("Checkbox 4 is checked")
        Focus += 1
    if check_var_4.get() == 1:
        print("Checkbox 5 is checked")
        Focus += 1

    print("Focus bien la : " + str(Focus))
    window.after(1000, window.destroy)
label_thuthang.pack(anchor="center")
submit_button = tk.Button(window, text="Next", command=submit,font=("Helvetica",11))
submit_button.pack()

# Tắt window sau 30 giây
window.after(300000, window.destroy)

# Chạy vòng lặp chính của giao diện
window.mainloop()

# Tạo một Turtle
t = turtle.Turtle()

# Point Openess
x3, y3 = 0, 250

# Point Courage
x4, y4 = 0, -250

# Point Commitment
x1, y1 = -250, 0

# Point Respect
x2, y2 = 250, 0

# Di chuyển Turtle đến điểm đầu tiên
# draw Commitment
t.penup()
t.goto(x1, 250)
t.pendown()
t.write("Commitment")
for i in range(5):
    t.goto(x1 + 50 * i, 50 * (5 - i))
    t.goto(x1 + 50 * i, 50 * (5 - i) + 5)
    t.goto(x1 + 50 * i, 50 * (5 - i) - 5)
    t.goto(x1 + 50 * i, 50 * (5 - i))

t.goto(0, 0)
# Vẽ đoạn thẳng từ điểm đầu tiên đến điểm thứ
# draw Respect
for i in range(1, 6):
    t.goto(50 * i, -50 * i)
    t.goto(50 * i, -50 * i + 5)
    t.goto(50 * i, -50 * i - 5)
    t.goto(50 * i, -50 * i)
t.write("Courage")
t.goto(0, 0)

# draw openness
for i in range(4, -1, -1):
    t.goto(0, y3 - 50 * i)
    t.goto(5, y3 - 50 * i)
    t.goto(-5, y3 - 50 * i)
    t.goto(0, y3 - 50 * i)

t.goto(x3, y3)
t.write("Openness")
t.goto(0, 0)

# draw courage
for i in range(1, 6):
    t.goto(-50 * i, -50 * i)
    t.goto(-50 * i, -50 * i + 5)
    t.goto(-50 * i, -50 * i - 5)
    t.goto(-50 * i, -50 * i)
t.write("Focus")
t.goto(0, 0)
t.goto(0, 0)

# draw respect
for i in range(1, 6):
    t.goto(50 * i, 50 * i)
    t.goto(50 * i, 50 * i + 5)
    t.goto(50 * i, 50 * i - 5)
    t.goto(50 * i, 50 * i)

t.goto(250, 250)
t.write("Respect")
t.goto(0, 0)

#print(type(Commitment))
# draw scrum values
t.goto(-50 * int(Commitment), 50 * int(Commitment))
t.pencolor("red")
t.goto(0, 50 * int(Openness))
t.goto(50 * int(Respect), 50 * int(Respect))
t.goto(50 * int(Courage), -50 * int(Courage))
t.goto(-50 * int(Focus), -50 * int(Focus))
t.goto(-50 * int(Commitment), 50 * int(Commitment))

# Đóng cửa sổ Turtle khi hoàn thành
turtle.done()
