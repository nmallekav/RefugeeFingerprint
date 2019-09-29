import tkinter as tk
from hash import get_hash
from refugee_sql_client import SqlClient

class app2:

    def __init__(self):
        self.sql_client = SqlClient()
        master = tk.Tk()
        tk.Label(master,
                 text="Picture").grid(row=0)


        self.e1 = tk.Entry(master)


        self.e1.grid(row=0, column=1)

        tk.Button(master,
                  text='Quit',
                  command=master.quit).grid(row=4,
                                            column=0,
                                            sticky=tk.W,
                                            pady=4)
        tk.Button(master,
                  text='Show', command=self.getInfo).grid(row=4,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

        

        tk.mainloop()


    def getInfo(self):
        filename = self.e1.get()
        h = hash(filename)
        txt = str(self.sql_client.lookUp(h))

        root = tk.Tk()
        T = tk.Text(root, height=2, width=30)
        T.pack()
        T.insert(tk.END, txt)
