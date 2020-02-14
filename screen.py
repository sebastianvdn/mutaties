# Import modules
from tkinter import Tk, Label, Entry, Button
import json
from datetime import date
import csv 

class AddNewPolicy():
    def __init__(self):
        # Create the window
        self.date = date.today()
        self.formatted_date = self.date.strftime("%d/%m/%Y")
        window = Tk()

        # Set title of the window
        window.title("Enter a new activated policy")

        # Set the dimensions of the window
        window.geometry('620x200')

        # Create the labels
        policy_label = Label(window, text="Policy*")
        policy_label.grid(column=1, row=0)
        comment_label = Label(window, text='Commment*')
        comment_label.grid(column=2, row=0)
        admin_label = Label(window, text='Admin*')
        admin_label.grid(column=3, row=0)
        gpo_label = Label(window, text="GPO*")
        gpo_label.grid(column=4, row=0)

        required_label = Label(window, text="*All the values are required.")
        required_label.grid(column=0, row=3)

        # Create an entry for user input
        policy_label_txt = Entry(window,width=10)
        policy_label_txt.grid(column=1, row=1)
        comment_label_txt = Entry(window, width=20)
        comment_label_txt.grid(column=2, row=1)
        admin_label_txt = Entry(window, width= 10)
        admin_label_txt.grid(column=3, row=1)
        gpo_label_txt = Entry(window, width=10)
        gpo_label_txt.grid(column=4, row=1)

        # Function that will be executed when clicked    
        def submit():
            global new_policy
            new_policy = {
                'policy': policy_label_txt.get(),
                'comment': comment_label_txt.get(),
                'admin': admin_label_txt.get(),
                'gpo': gpo_label_txt.get(),
                "date": self.formatted_date
            }

            with open('policies.json') as f:
                policies = json.load(f)
                temp = policies['applied_policies']

            def write_json(data, filename='policies.json'):
                """The function to add the data to the JSON file."""
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)            

            temp.append(new_policy)
            write_json(policies)

        def export():
            with open('policies.json') as f:
                data = json.load(f)

            for key, value in data.items():
                for item in value:
                    with open('policies.txt', 'a') as txt_file:
                        txt_file.write(f"\n{self.formatted_date}")
                        txt_file.write(
                            f"\npolicy: {item['policy']}\ncomment: {item['comment']}\nadmin: {item['admin']}\nGPO: {item['gpo']}\n"
                            )


        submit_btn = Button(window, text="submit", command=submit)
        submit_btn.grid(column=4, row=3)

        export_btn = Button(
            window, text="export (txt)",
            command=export)
        export_btn.grid(column=4, row=4)

        window.mainloop()


        

AddNewPolicy()