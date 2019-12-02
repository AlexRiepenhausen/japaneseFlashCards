from dataContainer import PandasData
from gui import Display
import tkinter as tk

if __name__ == '__main__':

    vocabulary = PandasData("C:/Users/PC/PycharmProjects/vocabulary/build/exe.win-amd64-3.7/data/vocabulary.csv",
                            "C:/Users/PC/PycharmProjects/vocabulary/build/exe.win-amd64-3.7/data/indices.txt")

    print('Welcome to my vocabulary tool')

    print('You have currently {} batch(es) of size 20 ({} words) stored in your revision box'.format(
        vocabulary.num_batches, 20*vocabulary.num_batches))

    print('Do you wish to generate a new batch?')
    yesno = input('[yes|no]: ')

    while yesno != 'yes' and yesno != 'no':
        yesno = input('Please type either yes or no: ')

    if yesno == "yes":
        vocabulary.generateNewBatch()
        vocabulary.writeBatchToFile()

    batchnum = input('Select batch number to be played (0-{}): '.format(vocabulary.num_batches-1))

    while not batchnum.isdigit():
        batchnum = input('Not a number, please try again: ')
        while int(batchnum) > vocabulary.num_batches-1 and int(batchnum) < 0:
            batchnum = input('Batch number does not exist, please try again: ')

    while int(batchnum) > vocabulary.num_batches - 1 and int(batchnum) < 0:
        batchnum = input('Batch number does not exist, please try again: ')


    refreshspeed = input('Select card refresh speed in seconds (minimum 1): ')

    while not refreshspeed.isdigit():
        refreshspeed = input('Not a number, please try again: ')
        while int(refreshspeed) < 1:
            refreshspeed = input('Smaller than 1, please try again: ')

    while int(refreshspeed) < 1:
        refreshspeed = input('Smaller than 1, please try again: ')


    root = tk.Tk()
    root.title("日本語のボキャブラリー")
    root.configure(background='white smoke')
    root.lift()
    app  = Display(vocabulary, int(batchnum), int(refreshspeed), master=root)
    app.mainloop()
