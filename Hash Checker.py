from pandas.io import clipboard
from tkinter import PhotoImage, Tk, ttk, END, IntVar, filedialog, messagebox
import hashlib


NAME = "HASH CHECKER"
VERSION = 2.0


class GetHash:
    def __init__(self):
        self.path = filedialog.askopenfilename()

    def get_hash256(self):
        if self.path != '':
            with open(self.path, 'rb') as file:
                byte = file.read()
                return hashlib.sha256(byte).hexdigest()

    def get_hash512(self):
        if self.path != '':
            with open(self.path, 'rb') as file:
                byte = file.read()
                return hashlib.sha512(byte).hexdigest()

    def get_hash_md5(self):
        if self.path != '':
            with open(self.path, 'rb') as file:
                byte = file.read()
                return hashlib.md5(byte).hexdigest()


class HashChecker(Tk, GetHash):
    def __init__(self):
        super(HashChecker, self).__init__()
        self.title(f"{NAME} [{VERSION}]")                               
        self.resizable(False, False)                                  
        ph = PhotoImage(file="images/icone.png")                       
        self.iconphoto(False, ph)                                       

    def main_window(self):
        def core():
            list_opts = [var_1.get(), var_2.get(), var_3.get()]
            
            if list_opts == [0, 0, 0]:
                messagebox.showwarning("Atenção", "Selecione uma opção.")

            else:
                GetHash.__init__(self)
                path_output.delete(0, END)
                path_output.insert(0, self.path)
                
                if 1 in list_opts:
                    hash_result = self.get_hash256()
                    if hash_result is not None:
                        output_sha256.delete(0, END)
                        output_sha256.insert(0, hash_result)

                if 2 in list_opts:
                    hash_result = self.get_hash512()
                    if hash_result is not None:
                        output_sha512.delete(0, END)
                        output_sha512.insert(0, hash_result)

                if 3 in list_opts:
                    hash_result = self.get_hash_md5()
                    if hash_result is not None:
                        output_md5.delete(0, END)
                        output_md5.insert(0, hash_result)

        def copy_sha256():
            clipboard.copy(output_sha256.get())

        def copy_sha512():
            clipboard.copy(output_sha512.get())

        def copy_md5():
            clipboard.copy(output_md5.get())

        frame = ttk.Frame(self)
        frame.grid(row=0, column=0)

        lbf_select = ttk.LabelFrame(frame, text="Selecione o arquivo")
        lbf_select.grid(row=0, column=0, padx=5, pady=5, sticky='N')
        label_select = ttk.Label(lbf_select, text="Arquivo selecionado: ")
        label_select.grid(row=0, column=0)
        path_output = ttk.Entry(lbf_select, width=55)
        path_output.grid(row=0, column=1, padx=5, pady=5)
        btt_get_hash = ttk.Button(lbf_select, text="Selecionar e verificar", command=core)
        btt_get_hash.grid(row=0, column=2)

        lbf_result = ttk.LabelFrame(frame, text="Resultado")
        lbf_result.grid(row=1, column=0, padx=5, pady=5, sticky='W')

        var_1 = IntVar()
        rd_btt_1 = ttk.Checkbutton(lbf_result, text="SHA 256", variable=var_1, onvalue=1, offvalue=0)
        rd_btt_1.grid(row=0, column=0, sticky="W", padx=5)
        output_sha256 = ttk.Entry(lbf_result, width=70)
        output_sha256.grid(row=0, column=2)
        btt_copy_sha256 = ttk.Button(lbf_result, text="Copiar", command=copy_sha256)
        btt_copy_sha256.grid(row=0, column=3, padx=5)

        var_2 = IntVar()
        rd_btt_2 = ttk.Checkbutton(lbf_result, text="SHA 512", variable=var_2, onvalue=2, offvalue=0)
        rd_btt_2.grid(row=1, column=0, sticky="W", padx=5)
        output_sha512 = ttk.Entry(lbf_result, width=70)
        output_sha512.grid(row=1, column=2)
        btt_copy_sha512 = ttk.Button(lbf_result, text="Copiar", command=copy_sha512)
        btt_copy_sha512.grid(row=1, column=3, padx=5)

        var_3 = IntVar()
        rd_btt_3 = ttk.Checkbutton(lbf_result, text="MD5", variable=var_3, onvalue=3, offvalue=0)
        rd_btt_3.grid(row=2, column=0, sticky="W", padx=5)
        output_md5 = ttk.Entry(lbf_result, width=70)
        output_md5.grid(row=2, column=2)
        btt_copy_md5 = ttk.Button(lbf_result, text="Copiar", command=copy_md5)
        btt_copy_md5.grid(row=2, column=3, padx=5)


if __name__ == "__main__":
    app = HashChecker()
    app.main_window()
    app.mainloop()
