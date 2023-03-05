#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Készíts egy függvényt ami paraméterként egy listát vár és visszatér ennek a listának egy rész listájával.
#Paraméterként lehessen megadni, hogy mettől-meddig akarjuk visszakapni a listát.
#Egy példa a bemenetre: input_list=[1,2,3,4,5], start=1, end=4
#Egy példa a kimenetre: [2,3,4]
#NOTE: ha indexelünk és 4-et adunk meg felső határnak akkor csak a 3. indexig kapjuk vissza az értékeket a 4. már nem lesz benne
#NOTE: és ez az elvárt viselkedés ebben a feladatban is
#return type: list
#függvény neve legyen: subset

input_list=[1,2,3,4,5]
start=1
end=4


# In[4]:


def subset(input_list, start, end):
    return input_list[start:end]
subset(input_list, start, end)


# In[7]:


#Készíts egy függvényt ami egy listát vár paraméterként és ennek a listának minden n-edik elemét adja vissza.
#Paraméterként lehessen állítani azt hogy hanyadik elemeket szeretnénk viszakapni.
#NOTE: a 0. elem is legyen benne
#Egy példa a bemenetre: input_list=[1,2,3,4,5,6,7,8,9], n=3
#Egy példa a kimenetre: [1,4,7]
#return type: list
#függvény neve legyen: every_nth
input_list=[1,2,3,4,5,6,7,8,9]
n=3


# In[6]:


def every_nth(input_list,n):
    return input_list[::n]
every_nth(input_list, n)


# In[9]:


#Készíts egy függvényt ami paraméterként egy listát vár és eldönti, hogy a listában csak egyedi értékek vannak-e
#Egy bool-al térjen vissza: True:csak egyedi értékek vannak benne, False:van benne ismétlődés
#Egy példa a bemenetre: [1,2,3,4,5,6,7]
#Egy példa a kimenetre: True
#return type: bool
#függvény neve legyen: unique
input_list = [1,2,3,4,5,6,7]


# In[8]:


def unique(input_list):
    return len(input_list) == len(set(input_list))
unique(input_list)


# In[13]:


#Készíts egy függvényt ami paraméterként egy 2 dimenziós listát vár és ezt a listát kitudja "lapítani"
#Egy olyan listával térjen vissza amelyben nincsen több kisebb lista, azaz egy egy dimenziós listával.
#Egy példa a bemenetre: [[1,2],[3,4],[5,6]]
#Egy példa a kimenetre: [1,2,3,4,5,6]
#NOTE: csak 2 dimenziós listát kezeljen nem kell ennél mélyebbet
#return type: list
#függvény neve legyen: flatten
input_list = [[1,2],[3,4],[5,6]]


# In[12]:


def flatten(lst):
    flattened_list = []
    for sublist in lst:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list
flatten(input_list)


# In[15]:


#Készíts egy függvényt ami paraméterként n darab listát vár, és összfűzi ezeket a listákat.
#Egy olya listával térjen vissza ami 1 dimenziós és tartalmazza az össze bemeneti lista kértékét
#NOTE: sorrend nem számít
#HINT: használj *args-ot az input paraméternél
#Egy példa a bemenetre: lista_1 = [1,2,3], lista_2 = [4,5,6], ..... lista_n = [7,8,9]
#Egy példa a kimenetre: [1,2,3,4,5,6,7,8,9]
#return type: list
#függvény neve legyen: merge_lists
lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]


# In[14]:


def merge_lists(*args):
    merged_list = []
    for arg in args:
        merged_list.extend(arg)
    return merged_list
merge_lists(lista_1, lista_2, lista_3)


# In[17]:


#Készíts egy függvényt ami paraméterként egy listát vár amiben 2 elemet tartalmazó tuple-ök vannak,
#és visszatér ezeknek a tuple-nek a fordítottjával.
#Egy példa a bemenetre: [(1,2),(3,4)]
#Egy példa a kimenetre: [(2,1),(4,3)] 
#return type: list
#függvény neve legyen: reverse_tuples
input_list = [(1,2),(3,4)]


# In[16]:


def reverse_tuples(input_list):
    reversed_list = [(a, b) for (b, a) in input_list]
    return reversed_list
reverse_tuples(input_list)


# In[19]:


#Készíts egy függvényt ami paraméterként egy listát vár, és eltávolítja az ismétlődéseket a listából.
#Egy olyan listával térjen vissza amiben csak a bemeneti lista egyedi értékei vannak benne.
#Egy példa a bemenetre: [1,2,3,3,4,5]
#Egy példa a kimenetre: [1,2,3,4,5]
#return type: list
#függvény neve legyen: remove_duplicates
input_list = [1,2,3,3,4,5]


# In[18]:


def remove_duplicates(input_list):
    return list(set(input_list))
remove_duplicates(input_list)


# In[21]:


#Készíts egy olyan függvényt ami paraméterként egy 2 dimenziós mátrixot vár és visszater a mátrix transzponáltjával.
#Egy példa a bemenetre: [[1,2,3],
#                        [4,5,6],
#                        [7,8,9]]
#
#Egy példa a kimenetre: [[1,4,7],
#                        [2,5,8],
#                        [3,6,9]]
#return type: list
#függvény neve legyen: transpose
input_list = [[1,2,3],
              [4,5,6],
              [7,8,9]]


# In[20]:


def transpose(input_list):
    return [list(row) for row in zip(*input_list)]
transpose(input_list)


# In[23]:


#Készíts egy függvényt ami paraméterként egy listát vár és visszatér a lista csoportosított változatával.
#Egy olyan listával térjen vissza amiben a paraméterként átadott chunk_size méretű listák vannak.
#Egy példa a bemenetre: [1,2,3,4,5,6,7,8]
#Egy példa a kimenetre: [[1,2,3],[4,5,6],[7,8]]
#NOTE: ha nem mindegyik lista elemet lehet chunk_size méretű listába tenni akkor a maradékot a példában látott módon kezeljétek
#return type: list
#függvény neve legyen: split_into_chunks
input_list = [1,2,3,4,5,6,7,8]
chunk_size = 3


# In[22]:


def split_into_chunks(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]
split_into_chunks(input_list, chunk_size)


# In[36]:


#Készíts egy függvényt ami paraméterként n darab dictionary-t vár és visszatér egy darab dictionary-vel.
#Egy olyan dict-el térjen vissza miben az n darab bemeneti dict értékei benne vannak.
#Egy példa a bemenetre: dict_1: {"one":1,"two":2}, dict_2: {"four":4,"three":3}
#Egy példa a kimenetre: {"one":1,"two":2,"four":4,"three":3}
#HINT: használj *args-ot
#függvény neve legyen: merge_dicts
dict_1 = {"one":1,"two":2}
dict_2 = {"four":4,"three":3}


# In[34]:


def merge_dicts(*args):
    result_dict = {}
    for arg in args:
        result_dict.update(arg)
    return result_dict
merge_dicts(dict_1,dict_2)


# In[38]:


#Készíts egy függvényt ami paraméterként egy listát vár amiben egész számok vannak és visszatér egy dict-el amiben szét vannak szedve paritás szerint.
#Egy példa a bemenetre: [1,2,3,4,5,6]
#Egy példa a kimenetre: {"event":[2,4,6],"odd":[1,3,5]}
#return type: dict
#függvény neve legyen: by_parity
input_list = [1,2,3,4,5,6]


# In[37]:


def by_parity(input_list):
    result = {"even": [], "odd": []}
    for number in input_list:
        if number % 2 == 0:
            result["even"].append(number)
        else:
            result["odd"].append(number)
    return result
by_parity(input_list)


# In[40]:


#Készíts egy függvényt ami paraméterként egy dict-et vár és visszatér egy dict-el amiben az egyes kulcsokhoz tartozó értékek átlaga van.
#Egy példa a bemenetre:{"some_key":[1,2,3,4],"another_key":[1,2,3,4]}
#Egy példa a kimenetre: {"some_key":2.5,"another_key":2.5}
#return type: dict
#függvény neve legyen: mean_key_value
input_dict = {"some_key":[1,2,3,4],"another_key":[1,2,3,4]}


# In[39]:


def mean_key_value(input_dict):
    result = {}
    for key, values in input_dict.items():
        result[key] = sum(values) / len(values)
    return result
mean_key_value(input_dict)


# In[ ]:


#Ha végeztél a feladatokkal akkor ezt a jupytert alakítsd át egy .py file-ra 
#ha vscode-ban dolgozol: https://stackoverflow.com/questions/64297272/best-way-to-convert-ipynb-to-py-in-vscode
#ha jupyter lab-ban dolgozol: https://stackoverflow.com/questions/52885901/how-to-save-python-script-as-py-file-on-jupyter-notebook


