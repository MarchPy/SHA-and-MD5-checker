import core
import tkinter as tk
from pandas.io import clipboard
from tkinter import END, Toplevel, ttk, filedialog, messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SHA and MD5 checker")
        self.resizable(False, False)

    def main_window(self):
        messagebox.showinfo("Atenção", "Arquivos muito grandes podem demorar mais!")

        def window_compare():
            def getvalues():
                value_1 = entry_value_1.get()
                value_2 = entry_value_2.get()
                if value_1 == value_2:
                    messagebox.showinfo("Sucesso", "O valores são iguais.")
                else:
                    messagebox.showerror("Ops", "Os valores não são iguais.")
                new_window.destroy()

            new_window = Toplevel(frame)
            
            label_value_1 = ttk.Label(new_window, text="1° Valor")
            label_value_1.grid(row=0, column=0)
            entry_value_1 = ttk.Entry(new_window, width=25)
            entry_value_1.grid(row=0, column=1, padx=5, pady=5, sticky='E')

            label_value_2 = ttk.Label(new_window, text="2° Valor")
            label_value_2.grid(row=1, column=0)
            entry_value_2 = ttk.Entry(new_window, width=25)
            entry_value_2.grid(row=1, column=1, padx=5, pady=5, sticky='E')

            button_compare_2 = ttk.Button(new_window, text="Comparar", command=getvalues)
            button_compare_2.grid(row=2, column=1, sticky='E', padx=5, pady=5)

        def get_path():
            entry_label.delete(0, END)
            entry_label_sha256.delete(0, END)
            entry_label_sha512.delete(0, END)
            entry_label_md5.delete(0, END)

            path = filedialog.askopenfilename()
            entry_label.insert(0, path)

            li = [var_1.get(), var_2.get(), var_3.get()]

            if li[0] == 0:
                result = core.check(path, '256')
                entry_label_sha256.insert(0, result)
            
            if li[1] == 2:
                result = core.check(path, '512')
                entry_label_sha512.insert(0, result)

            if li[2] == 3:
                result = core.check(path, 'md5')
                entry_label_md5.insert(0, result)

        def copy_sha256():
            result = entry_label_sha256.get()
            clipboard.copy(result)

        def copy_sha512():
            result = entry_label_sha512.get()
            clipboard.copy(result)

        def copy_md5():
            result = entry_label_md5.get()
            clipboard.copy(result)

        frame = ttk.Frame(self)
        frame.grid(row=0, column=0)

        label_frame_1 = ttk.LabelFrame(frame, text="Selecione o arquivo")
        label_frame_1.grid(row=0, column=0, padx=5, pady=5, ipadx=3, sticky='W')
        label_1 = ttk.Label(label_frame_1, text="Caminho: ")
        label_1.grid(row=0, column=0, sticky='W')
        entry_label = ttk.Entry(label_frame_1, width=45)
        entry_label.grid(row=0, column=1)
        button_search = ttk.Button(label_frame_1, text="Procurar", command=get_path)
        button_search.grid(row=0, column=2, padx=5, pady=5, sticky='E')

        label_frame_2 = ttk.LabelFrame(frame, text="Selecione a criptografia")
        label_frame_2.grid(row=0, column=1, padx=5, pady=5)
        var_1 = tk.IntVar()
        var_2 = tk.IntVar()
        var_3 = tk.IntVar()
        radio_1 = ttk.Checkbutton(label_frame_2, text="SHA256", variable=var_1, onvalue=0, offvalue=1)
        radio_1.grid(row=0, column=0, sticky='W')
        radio_2 = ttk.Checkbutton(label_frame_2, text="SHA512", variable=var_2, onvalue=2, offvalue=0)
        radio_2.grid(row=1, column=0, sticky='W')
        radio_3 = ttk.Checkbutton(label_frame_2, text="MD5", variable=var_3, onvalue=3, offvalue=0)
        radio_3.grid(row=2, column=0, sticky='W')

        label_frame_3 = ttk.LabelFrame(frame, text="Resultado")
        label_frame_3.grid(row=1, column=0, padx=5, pady=5, sticky='W')
        label_sha256 = ttk.Label(label_frame_3, text="SHA256")
        label_sha256.grid(row=0, column=0, sticky='W')
        entry_label_sha256 = ttk.Entry(label_frame_3, width=60)
        entry_label_sha256.grid(row=0, column=1, padx=5, pady=5)
        button_copy_1 = ttk.Button(label_frame_3, text="Copiar", command=copy_sha256)
        button_copy_1.grid(row=0, column=2)
        label_sha512 = ttk.Label(label_frame_3, text="SHA512")
        label_sha512.grid(row=1, column=0, sticky='W')
        entry_label_sha512 = ttk.Entry(label_frame_3, width=60)
        entry_label_sha512.grid(row=1, column=1, padx=5, pady=5)
        button_copy_2 = ttk.Button(label_frame_3, text="Copiar", command=copy_sha512)
        button_copy_2.grid(row=1, column=2)
        label_md5 = ttk.Label(label_frame_3, text="MD5")
        label_md5.grid(row=2, column=0, sticky='W')
        entry_label_md5 = ttk.Entry(label_frame_3, width=60)
        entry_label_md5.grid(row=2, column=1, padx=5, pady=5)
        button_copy_3 = ttk.Button(label_frame_3, text="Copiar", command=copy_md5)
        button_copy_3.grid(row=2, column=2)

        label_frame_4 = ttk.LabelFrame(frame, text="Opções")
        label_frame_4.grid(row=1, column=1, padx=5, pady=5, sticky='N')
        button_compare_1 = ttk.Button(label_frame_4, text="Comparar Valores", command=window_compare)
        button_compare_1.grid(row=0, column=0, sticky='N', padx=5, pady=5)


if __name__ == "__main__":
    program = App()
    program.main_window()
    program.mainloop()
