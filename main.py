import os
import re
dataSet_path = './Dataset_IR'
train_path = dataSet_path + '/train'
test_path = dataSet_path + '/test'

dir_path = os.listdir(dataSet_path)

# print(dir_path)


def find_dataSet(symbol , dataset_dir):

    pattern_string = ".*"+ symbol + ".*txt$"

    for root , dirs , files in os.walk(dataset_dir):
        for file in files:
            if (re.match(pattern_string , file)):
                return os.path.join(root, file)


a = find_dataSet('khasapa' , dataSet_path)


f = open(a , encoding="utf8")

print(f.read())








