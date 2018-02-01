
# coding: utf-8

# In[1]:

import json
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
#get_ipython().magic('matplotlib inline')
import re


# ## Read json file

# In[2]:

import json

j_list = []
with open("data.json") as f:
    for line in f:
        j_content = json.loads(line)
        j_list.append(j_content)
#print (j_list)


# In[3]:

len(j_list)


# ## 1. Return every unique locality (cf. city) along with how often it occurs

# In[4]:

city = {}
total_num = 0
for i in range(len(j_list)):
    if not j_list[i]['payload']:
        continue
    total_num += 1
    name = j_list[i]['payload']['country'] + '-' + j_list[i]['payload']['locality']
    city[name] = city.get(name, 0) + 1
    
for key, value in city.items():
    city[key] = value/total_num  # normalize the occurrence times for each unique city 
    #print (key, city[key])
print ('Result has been stored in Q1_ans.json')


# In[5]:

json = json.dumps(city)
f = open("Q1_ans.json","w")
f.write(json)
f.close()


# In[6]:

# Here is the result:
city


# In[32]:

sorted_city = sorted(list(city.keys()))
plt.figure(figsize=(20,5))
plt.bar(range(len(city)), [city[x] for x in sorted_city], color='g')
plt.xticks(range(0,len(city),20),sorted_city[::20])
plt.ylabel('Probability')
plt.xlabel('City')
plt.title('Distribution for City Occurrence')
plt.show()


# ## 2. Return all addresses that start with a number (return just the address)

# In[33]:

addresses = []
total_num = 0
for i in range(len(j_list)):
    if not j_list[i]['payload']:
        continue
    if 'address' not in j_list[i]['payload']:
        continue
    total_num += 1
    address = j_list[i]['payload']['address'].strip()
    if not address:
        continue
    if(re.search('[0-9]', address[0])):
        addresses.append(address)


# In[34]:

import json
my_json_string = json.dumps(addresses)
f = open("Q2_ans.json","w")
f.write(my_json_string)
f.close()


# In[35]:

print ('Result has been stored in Q2_ans.json')


# ## 3. Return all rows with addresses that don't contain a number (return the entire row)

# In[15]:

rows = []
for i in range(len(j_list)):
    if not j_list[i]['payload']:
        continue
    if 'address' not in j_list[i]['payload']:
        continue
    address = j_list[i]['payload']['address'].strip()
    if not address:
        continue
    if(re.search('[0-9]', address)):
        #addresses.append(re.sub ('[0-9]|-|/', '', address).strip())
        continue
    else:
        #print (address)
        rows.append(j_list[i])


# In[16]:

rows


# In[17]:

my_json_string = json.dumps(rows)
f = open("Q3_ans.json","w")
f.write(my_json_string)
f.close()


# In[18]:

print ('Result has been stored in Q3_ans.json')


# ## 4. Return the number of records that are museums

# In[19]:

count = 0
for i in range(len(j_list)):
    if not j_list[i]['payload']:
        continue
    if 'category_labels' not in j_list[i]['payload']:
        continue
    if re.search('museums', ''.join(j_list[i]['payload']['category_labels'][0]).lower()):
        count += 1
        
print ('The number of records that are museums: ',count)


# In[20]:

my_json_string = json.dumps(count)
f = open("Q4_ans.json","w")
f.write(my_json_string)
f.close()


# In[21]:

print ('Result has been stored in Q4_ans.json')


# ## 5. Return a new object containing uuid, name, website, and email address for all rows that have values for all four of these attributes; exclude any rows that don’t have all four

# In[22]:

record = []
dic = {}
for i in range(len(j_list)):
    if 'uuid' not in j_list[i] or 'payload' not in j_list[i]:
        continue
    
    if {'name','website','email'}.issubset(j_list[i]['payload']) == False:
        continue
    
    dic['uuid'] = j_list[i]['uuid']
    dic['name'] = j_list[i]['payload']['name']
    dic['website'] = j_list[i]['payload']['website']
    dic['email_address'] = j_list[i]['payload']['email']
    
    record.append(dic)


# In[23]:

len(record)


# In[24]:

my_json_string = json.dumps(record)
f = open("Q5_ans.json","w")
f.write(my_json_string)
f.close()


# In[25]:

print ('Result has been stored in Q5_ans.json')


# ## 6. Return all rows, but transform the names to all lower case while changing nothing else

# In[26]:

import copy
j_list_copy = j_list.copy()
for i in range(len(j_list_copy)):
    if 'payload' not in j_list_copy[i]:
        continue
    if 'name' not in j_list_copy[i]['payload']:
        continue
    j_list_copy[i]['payload']['name'] = j_list_copy[i]['payload']['name'].lower()


# In[27]:

my_json_string = json.dumps(j_list_copy)
f = open("Q6_ans.json","w")
f.write(my_json_string)
f.close()


# In[28]:

print ('Result has been stored in Q6_ans.json')


# ## 7.Return all rows for businesses that open before 10:00 a.m. on Sundays

# In[42]:

record = []
for i in range(len(j_list)):
    if 'payload' not in j_list[i]:
        continue
    if 'hours' not in j_list[i]['payload']:
        continue
        
    hours = json.loads(j_list[i]['payload']['hours'])
    
    if 'sunday' in hours:
        check = False
        for item in hours['sunday']:
            for s in item:
                if re.search(r'^([0-9]):[0-9][0-9]',s) or re.search(r'^([0][0-9]):[0-9][0-9]',s):
                    check = True
        if check:
            record.append(j_list[i])


# In[43]:

my_json_string = json.dumps(record)
f = open("Q7_ans.json","w")
f.write(my_json_string)
f.close()


# In[44]:

print ('Result has been stored in Q7_ans.json')


# In[45]:

len(record)


# In[ ]:



