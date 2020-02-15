# Import modules
from tkinter import Tk, Label, Entry, Button, ttk, messagebox
import json
from datetime import date
import xlsxwriter
from PIL import Image, ImageTk
import os 

class AddNewPolicy():
    def __init__(self):
        # Create the window
        self.date = date.today()
        self.formatted_date = self.date.strftime("%d/%m/%Y")
        window = Tk()

        # Set title of the window
        window.title("Enter a new activated policy")

        # Create the labels
        policy_label = Label(window, text="Policy")
        policy_label.grid(column=1, row=0)
        comment_label = Label(window, text='Commment')
        comment_label.grid(column=2, row=0)
        gpo_label = Label(window, text="GPO")
        gpo_label.grid(column=4, row=0)

        # Create a combo with predifined admins
        admin_label = Label(window, text='Admin')
        admin_label.grid(column=3, row=0)
        admin_combo = ttk.Combobox(window)
        admin_combo['values']= ('Sebastian', 'Wim', 'Jan', 'Fons')
        admin_combo.current(0)
        admin_combo.grid(column=3, row=1)

        # Create an image
        size = 100, 100
        image = Image.open('vives.png')
        image.thumbnail(size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)
        imgView = ttk.Label(window, image=render)
        imgView.grid(row=5, column=0, columnspan=2, sticky='S')

        # Create an entry for user input
        policy_label_txt = Entry(window,width=10)
        policy_label_txt.grid(column=1, row=1)
        comment_label_txt = Entry(window, width=20)
        comment_label_txt.grid(column=2, row=1)
        gpo_label_txt = Entry(window, width=10)
        gpo_label_txt.grid(column=4, row=1)

        # Function that will be executed when clicked on submit 
        def submit():
            if not policy_label_txt.get():
                messagebox.showwarning(
                    "Missing values", "You must fill in the policy!")
            if not comment_label_txt.get():
                messagebox.showwarning(
                    "Missing values", "You must fill in the comment!")
            if not admin_combo.get():
                messagebox.showwarning(
                    "Missing values", "You must choose an admin!")
            if not gpo_label_txt.get():
                messagebox.showwarning(
                    "Missing values", "You must tell to wich GPO it was aplied!")

            else:
                global new_policy
                new_policy = {
                    'policy': policy_label_txt.get(),
                    'comment': comment_label_txt.get(),
                    'admin': admin_combo.get(),
                    'gpo': gpo_label_txt.get(),
                    "date": self.formatted_date
                }

                with open('policies.json') as f:
                    policies = json.load(f)

                def write_json(data, filename='policies.json'):
                    """The function to add the data to the JSON file."""
                    with open(filename, 'w') as f:
                        json.dump(data, f, indent=4)            

                policies.append(new_policy)
                write_json(policies)
        
        # Function executed when clicked on export (txt)
        def export_txt():
            with open('policies.json') as f:
                data = json.load(f)

            for item in data:
                with open('policies.txt', 'a') as txt_file:
                    txt_file.write(f"\n{self.formatted_date}")
                    txt_file.write(
                        f"\npolicy: {item['policy']}\ncomment: {item['comment']}\nadmin: {item['admin'].title()}\nGPO: {item['gpo']}\n"
                        )

        # Function executed when clicked on export (xlsx)
        def export_xlsx():
            workbook = xlsxwriter.Workbook('policies.xlsx')
            worksheet = workbook.add_worksheet()

            bold = workbook.add_format({'bold': True})

            headers = [
                'policy', 'comment', 'admin', 'gpo', 'date'
            ]

            with open('policies.json') as f:
                policies = json.load(f)

            first_row = 0
            for header in headers:
                col = headers.index(header)
                worksheet.write(first_row, col, header, bold)

            row = 1
            for policy in policies:
                for _key, _value in policy.items():
                    col = headers.index(_key)
                    worksheet.write(row, col, _value)

                row += 1

            workbook.close()
            path = r"C:\Users\sebas\OneDrive - Hogeschool VIVES\Netwerkbeheer\Kwartaal3\Windows server\mutaties\policies.xlsx"
            os.system(path)


        submit_btn = Button(window, text="submit", command=submit, bg="red")
        submit_btn.grid(column=4, row=2)

        export_btn_txt = Button(
            window, text="export (txt)",
            command=export_txt, bg="green")
        export_btn_txt.grid(column=4, row=3)

        export_btn_xlsx = Button(
            window, text="export (xlsx)",
            command=export_xlsx, bg='green'
        )
        export_btn_xlsx.grid(column=4, row=4)

        window.mainloop()


AddNewPolicy()