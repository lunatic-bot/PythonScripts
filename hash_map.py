
# ## implementation of hash map 
# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]

    
#     def get_hash(self, key):
#         h = 0
#         for ch in key:
#             h += ord(ch)
        
#         return h % self.MAX
    

#     # def add(self, key, val):
#     #     h = self.get_hash(key)
#     #     self.arr[h] = val


#     ## set value of a key in hash map
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val

    
#     # def get(self, key):
#     #     h = self.get_hash(key)
#     #     return self.arr[h]
    
#     ## get value corresponding to a key
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         return self.arr[h]
    
#     ## delete the value for a given key
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.arr[h] = None

        
    
    

# t = HashTable()
# # print(t.get_hash('march 6'))
# # t.add('march 6', 130)
# t['march 7'] = 150
# t['march 6'] = 130
# t['march 9'] = 79
# print(t.arr)

# print(t['march 7'])

# del t['march 9']

# print(t.arr)



## collision handling

## implementation of hash map 
class HashTable:
    def __init__(self):
        self.MAX = 10
        ## list of linked list for collision handling
        self.arr = [[] for i in range(self.MAX)]

    
    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        
        return h % self.MAX
    

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val


    ## set value of a key in hash map
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key, val))



    
    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]
    
    ## get value corresponding to a key
    def __getitem__(self, key):
        h = self.get_hash(key)
        # return self.arr[h]
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    
    ## delete the value for a given key
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

        
    
    

t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
t['march 7'] = 150
t['march 6'] = 130
t['march 9'] = 79
t['march 17'] = 230
print(t.arr)

print(t['march 6'])
print(t['march 17'])

del t['march 17']

print(t.arr)
