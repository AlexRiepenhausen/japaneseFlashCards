import tkinter as tk

class Display(tk.Frame):

    def __init__(self, vocabulary, batchnum, refreshspeed, master=None):
        super().__init__(master)

        self.master       = master
        self.batchnum     = batchnum
        self.vocabulary   = vocabulary
        self.refreshspeed = refreshspeed

        self.master.attributes('-topmost', True)
        self.master.geometry("300x100+1220+10")

        self.kanji    = tk.Label(self, fg="blue",  background="white smoke")
        self.hiragana = tk.Label(self, fg="black", background="white smoke")
        self.english  = tk.Label(self, fg="black", background="white smoke")

        self.kanji.grid(row=0, column=0)
        self.hiragana.grid(row=1, column=0)
        self.english.grid(row=2, column=0)

        self.kanji.config(font="Helvetica 18")
        self.hiragana.config(font="Helvetica 12 bold")
        self.english.config(font="Helvetica 10 bold")

        self.pack()

        self.batch_index = 0

        self.updateVocab()


    def updateVocab(self):

        index = self.vocabulary.indices[self.batchnum][self.batch_index]
        self.kanji["text"]    = self.vocabulary.data[index]["KANJI"]
        self.hiragana["text"] = self.vocabulary.data[index]["HIRAGANA"]
        self.english["text"]  = str(self.vocabulary.data[index]["ENGLISH"])[:40]

        print(self.kanji["text"])
        print(self.hiragana["text"])
        print(self.english["text"])

        self.updateBatchIndex()

        self.after(self.refreshspeed*1000, self.updateVocab)


    def updateBatchIndex(self):
        self.batch_index += 1
        if self.batch_index == 20:
            self.batch_index = 0
