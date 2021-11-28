import pickle
import os

path='result.pkl'
output = 'mydividelabel/{}.txt'
if not os.path.exists('mydividelabel'):
    os.mkdir('mydividelabel')

data0 = open(path, 'rb')
data = pickle.load(data0)
# print(data[0])

for i in range(len(data)):
    num = len(data[i].get('name'))
    f = open(output.format(data[i].get('frame_id')), 'w+')
    int1 = int(data[i].get('frame_id'))
    for j in range(num):
        f.write(str(int1))
        f.write(' ')
        f.write(str(data[i].get('name')[j]))
        f.write(' ')
        # f.write(str(data[i].get('truncated')[j]))
        # f.write(' ')
        # f.write(str(data[i].get('occluded')[j]))
        # if data[i].get('occluded')[j] != 0:
        #     print(data[i].get('occluded')[j])
        # f.write(' ')
        for i1 in data[i].get('bbox')[j]:
            f.write(str(i1))
            f.write(' ')
        # f.write(str(data[i].get('bbox')[j]))
        f.write(str(data[i].get('score')[j]))
        f.write(' ')
        for i1 in data[i].get('dimensions')[j]:
            f.write(str(i1))
            f.write(' ')
        # f.write(str(data[i].get('dimensions')[j]))
        for i1 in data[i].get('location')[j]:
            f.write(str(i1))
            f.write(' ')
        # f.write(str(data[i].get('location')[j]))
        f.write(str(data[i].get('rotation_y')[j]))
        f.write(' ')
        f.write(str(data[i].get('alpha')[j]))
#         # f.write(' ')
#         # for i1 in data[i].get('boxes_lidar')[j]:
#         #     f.write(str(i1))
#         #     f.write(' ')
#         # f.write(str(data[i].get('boxes_lidar')[j]))
        f.write('\n')
    f.close()




