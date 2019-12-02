from random import *
import csv

''' class that reads data (e.g. csv or xml)
and converts them into a pandas data structure representation '''

class PandasData():

    def __init__(self, file_path, file_path_indices):

        self.file_path         = file_path
        self.file_path_indices = file_path_indices
        self.data              = None
        self.indices           = dict()
        self.num_batches       = 0
        self.number_of_words   = 0

        self.readVocabulary()
        self.readIndices()


    # read existing indices
    def readIndices(self):

        batch     = 0
        index_arr = list()

        with open(self.file_path_indices, 'r') as f:
            for line in f:
                line = line.rstrip("\n")
                if line != "----":
                    index = int(line)
                    index_arr.append(index)
                else:
                    self.indices[batch] = index_arr
                    batch = batch + 1
                    index_arr = list()

        self.num_batches = len(self.indices)



    # generate new batch
    def generateNewBatch(self):

        new_index_arr = list()

        while len(new_index_arr) < 20:
            index = randint(0, self.number_of_words - 1)
            while(self.indexExists(index)):
                index = randint(0, self.number_of_words - 1)
            new_index_arr.append(index)

        self.indices[self.num_batches] = new_index_arr
        self.num_batches += 1


    # check if index already present in dictionary
    def indexExists(self, index):
        for i in range(0, self.num_batches):
            if index in self.indices[i]:
                return True
        return False



    # write batches back to memory
    def writeBatchToFile(self):

        for batch in self.indices:
            array = self.indices[batch]

        with open(self.file_path_indices, 'w') as f:
            for batch in self.indices:
                array = self.indices[batch]
                for item in array:
                    f.write(str(item)+"\n")
                f.write("----\n")


    # reads keyword file and stores it in pandas data structure - out of service
    def readVocabulary(self):

        self.data = []
        cols = ["KANJI", "HIRAGANA", "ENGLISH"]

        with open(self.file_path, encoding="utf8") as file:
            csv_reader = csv.reader(file, delimiter=',')
            for line in csv_reader:
                kanji    = str(line[0])
                hiragana = str(line[1])
                english  = str(line[2])
                self.data.append({"KANJI": kanji, "HIRAGANA": hiragana, "ENGLISH": english})
                self.number_of_words += 1

