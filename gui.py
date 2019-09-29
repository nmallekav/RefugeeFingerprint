import tkinter as tk
from hash import get_hash
from refugee_sql_client import SqlClient
import os
from fingerprint_search import has_match

class app:

    def __init__(self):
        self.sql_client = SqlClient()
        master = tk.Tk()
        tk.Label(master,
                 text="Name").grid(row=0)
        tk.Label(master,
                 text="Date of birth").grid(row=1)
        tk.Label(master,
                 text="fingerprint-hash").grid(row=2)
        tk.Label(master,
                 text="gender").grid(row=3)

        fingerprints_files = os.listdir('database')

        

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e3 = tk.Entry(master)
        self.e4 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)

        tk.Button(master,
                  text='Quit',
                  command=master.quit).grid(row=4,
                                            column=0,
                                            sticky=tk.W,
                                            pady=4)
        tk.Button(master,
                  text='Show', command=self.show_entry_fields).grid(row=4,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

        tk.mainloop()

    def show_entry_fields(self):
        self.sql_client.insert_into(self.e1.get(), self.e2.get(), get_hash(self.e3.get()), self.e4.get())



