import pandas as pd

with open(r'C:\Users\Administrator\Desktop\xiaoxiaole_0802to0808.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

for i in range(26):
    print('\''+chr(i+ord('a'))+'\''+',', end='')
zimu = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(zimu)

data_msg = pd.read_csv(r'C:\Users\Administrator\Desktop\xiaoxiaole_0802to0808\xiaoxiaole_0802to0808.txt',
                       sep='|', header=None,
                       names=['a', 'b', 'c', 'd', 'e', 'f', 'g',
                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                              'o', 'p', 'q', 'r', 's', 't', 'u',
                              'v', 'w', 'x', 'y', 'z'])
data_msg_tmp = data_msg.loc[data_msg['a'].between(20190802,20190804)]
data_msg_tmp = data_msg_tmp.sort_values(by=['a', 'z'], ascending=True)


def My_to_csv(data_ys, csv_name):
    data = data_ys
    name = csv_name
    data.to_csv(r'C:\Users\Administrator\Desktop\{}.txt'.format(name),
                header=False, index=False)

My_to_csv(data_msg_tmp, 'xiaoxiaole_0802to0804')
