import pandas as pd

# import the file as pandas dataframe
df = pd.read_csv('passwords.csv',delimiter=' ')

# 	limits	character	password
# 0	3-4	l:	vdcv
# 1	6-9	d:	dddddkzdl
# 2	6-13	f:	mfswqfrqffrvfvf
# 3	10-12	l:	sfzlnwcptlnlflq
# 4	2-4	m:	qbwcmt
# ...	...	...	...
# 995	5-11	d:	wgwhfxtjmdfd
# 996	7-12	m:	chmmmrmrmxmqjcpmb
# 997	1-2	n:	nntnnn
# 998	4-12	l:	lllllllllllnllll
# 999	4-5	c:	ccchc

# minChar: the lowest number from the password policy
# maxChar: the highest number from the password policy
# character: the character that must be included in the password
minChar   = [i.split('-')[0] for i in df['limits'].to_list()]
maxChar   = [i.split('-')[1] for i in df['limits'].to_list()]
character = [i.split(':')[0] for i in df['character'].to_list()]

# create dictionary of the arrays
data = {'minChar': minChar,
        'maxChar': maxChar,
        'character': character,
        'password': df['password'].to_list()}

# create dataframe
df = pd.DataFrame(data)

# minChar	maxChar	character	password
# 0	3	4	l	vdcv
# 1	6	9	d	dddddkzdl
# 2	6	13	f	mfswqfrqffrvfvf
# 3	10	12	l	sfzlnwcptlnlflq
# 4	2	4	m	qbwcmt
# ...	...	...	...	...
# 995	5	11	d	wgwhfxtjmdfd
# 996	7	12	m	chmmmrmrmxmqjcpmb
# 997	1	2	n	nntnnn
# 998	4	12	l	lllllllllllnllll
# 999	4	5	c	ccchc

# the valid password counter
validPassCounter = 0
for index, row in df.iterrows():
    # row is a pandas series
    # convert row to dictionary
    data = row.to_dict()
    # get the desired position of the character in the password
    ps1 = int(data['minChar']) - 1
    ps2 = int(data['maxChar']) - 1
    # check if the character is in the correct positions
    if len(data['password']) - 1 >= ps2:
        if data['password'][ps1] != data['password'][ps2]:
            if data['password'][ps1] == data['character'] or data['password'][ps2] == data['character']:
                validPassCounter += 1
                continue

print('There are', validPassCounter, 'valid passwords')