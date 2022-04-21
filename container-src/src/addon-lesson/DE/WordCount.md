# Word Count

::: tip Download dataset

<a href="/DE/dataset.txt" download>Click here for download dataset</a>

Thank you, [RealPython](https://realpython.com/start-here/) for your blog.
:::


## project structure
```
+-- word-count
|    +-- dataset.txt
|    +-- main.py
```

dataset.txt

<<< @/src/.vuepress/public/DE/dataset.txt

## Let's start coding together
```py
dataset = None
with open("dataset.txt","r") as dataset_file:
    dataset = dataset_file.readlines()
print(dataset)
```

:::output
['What Pythonistas Are Saying:\n', '\n', 'Real Python has been around since 2012. And ever since the first days, we’ve been grateful to affect the “Python Journey” of so many readers like you. Here’s what some of them had to say about us:\n', '\n', '“Real Python is an awesome resource for the budding developer. Not only will you learn Python, you will learn how to use it as you build practical and functional web-based applications.”\n', '\n', '— Jared Nielsen\n', '\n', '“You do a wonderful job of explaining and teaching Python in a way that people like me, a complete novice, could really grasp. I think you have a gift for making Python seem more attainable to people outside the programming world. This is something I never thought I would be doing or learning and with a little push from you I am learning it and I can see that it will be nothing but beneficial to me in the future.”\n', '\n', '— Shea Klusewicz\n', '\n', '“The best way to learn Python without killing yourself is Real Python!!”\n', '\n', '— Stavros Anastasiadis\n', '\n', '“I’ve been using Python for two years, and my skills have increased over time. I’ve been able to do this by constantly trying to learn new concepts, of OOP programming for example, and different Python coding strategies like decorators or list comprehensions.\n', '\n', 'I will then go out and build my own stuff. Once I get tired of implementing the same coding concepts, and want to do something new and better, I’ll go back to the drawing board and learn more coding. This cycle has helped me retain what I’ve learned and keep growing.\n', '\n', 'Reading what Real Python has to say, like their blog and books, will help you achieve this.”\n', '\n', '— Aaron Lelevier']
:::

```py
dataset = None
with open("dataset.txt","r") as dataset_file:
    dataset = dataset_file.readlines()

words = {}
for each_line in dataset:
    each_line = each_line.replace("\n","")
    each_line = each_line.replace(",","")
    each_line = each_line.replace(".","")
    each_line = each_line.replace("!","")
    each_line = each_line.replace("’","")
    each_line = each_line.replace("“","")
    each_line = each_line.replace('”',"")
    each_line = each_line.replace('-',"")
    each_line = each_line.replace(':',"")

    word_line = each_line.split()
    
    for word in word_line:
        word = word.lower()
        if word not in words:
            words[word] = 0
        words[word] = words[word] + 1

print(words)
```
:::output
{'what': 4, 'pythonistas': 1, 'are': 1, 'saying': 1, 'real': 4, 'python': 11, 'has': 3, 
'been': 4, 'around': 1, 'since': 2, '2012': 1, 'and': 13, 'ever': 1, 'the': 8, 'first': 1,
 'days': 1, 'weve': 1, 'grateful': 1, 'to': 11, 'affect': 1, 'journey': 1, 'of': 5, 'so': 1, 
 'many': 1, 'readers': 1, 'like': 4, 'you': 8, 'heres': 1, 'some': 1, 'them': 1, 'had': 1, 'say': 2, 
 'about': 1, 'us': 1, 'is': 3, 'an': 1, 'awesome': 1, 'resource': 1, 'for': 4, 'budding': 1, 'developer': 1, 
 'not': 1, 'only': 1, 'will': 5, 'learn': 5, 'how': 1, 'use': 1, 'it': 3, 'as': 1, 'build': 2, 'practical': 1,
  'functional': 1, 'webbased': 1, 'applications': 1, '—': 4, 'jared': 1, 'nielsen': 1, 'do': 3, 'a': 5,
   'wonderful': 1, 'job': 1, 'explaining': 1, 'teaching': 1, 'in': 2, 'way': 2, 'that': 2, 'people': 2, 'me': 3, 
   'complete': 1, 'novice': 1, 'could': 1, 'really': 1, 'grasp': 1,
  'i': 7, 'think': 1, 'have': 2, 'gift': 1, 'making': 1, 'seem': 1, 'more': 2, 'attainable': 1, 'outside': 1, 
  'programming': 2, 'world': 1, 'this': 4, 'something': 2, 'never': 1,
'thought': 1, 'would': 1, 'be': 2, 'doing': 1, 'or': 2, 'learning': 2, 'with': 1, 'little': 1, 'push': 1, 
'from': 1, 'am': 1, 'can': 1, 'see': 1, 'nothing': 1, 'but': 1, 
'beneficial': 1, 'future': 1, 'shea': 1, 'klusewicz': 1, 'best': 1, 'without': 1, 'killing': 1, 'yourself': 1, 
'stavros': 1, 'anastasiadis': 1, 'ive': 3, 'using': 1, 'two': 1,
 'years': 1, 'my': 2, 'skills': 1, 'increased': 1, 'over': 1, 'time': 1, 'able': 1, 'by': 1, 'constantly': 1, 'trying': 1, 
 'new': 2, 'concepts': 2, 'oop': 1, 'example': 1,
  'different': 1, 'coding': 3, 'strategies': 1, 'decorators': 1, 'list': 1, 'comprehensions': 1, 'then': 1, 'go': 2, 'out': 1, 
  'own': 1, 'stuff': 1, 'once': 1, 'get': 1, 
  'tired': 1, 'implementing': 1, 'same': 1, 'want': 1, 'better': 1, 'ill': 1, 'back': 1, 'drawing': 1, 
  'board': 1, 'cycle': 1, 'helped': 1, 'retain': 1, 'learned': 1, 'keep': 1, 
  'growing': 1, 'reading': 1, 'their': 1, 'blog': 1, 'books': 1, 'help': 1, 'achieve': 1, 'aaron': 1, 'lelevier': 1}
:::

```py{25-30}
dataset = None
with open("dataset.txt","r") as dataset_file:
    dataset = dataset_file.readlines()

words = {}
for each_line in dataset:
    each_line = each_line.replace("\n","")
    each_line = each_line.replace(",","")
    each_line = each_line.replace(".","")
    each_line = each_line.replace("!","")
    each_line = each_line.replace("’","")
    each_line = each_line.replace("“","")
    each_line = each_line.replace('”',"")
    each_line = each_line.replace('-',"")
    each_line = each_line.replace(':',"")

    word_line = each_line.split()
    
    for word in word_line:
        word = word.lower()
        if word not in words:
            words[word] = 0
        words[word] = words[word] + 1

removed_word = []
for word in words:
    if words[word] <= 1:
        removed_word.append(word)
for rw in removed_word:
    del words[rw]

print(words)
```
:::output
{'what': 4, 'real': 4, 'python': 11, 'has': 3, 'been': 4, 
'since': 2, 'and': 13, 'the': 8, 'to': 11, 'of': 5, 'like': 4, 
'you': 8, 'say': 2, 'is': 3, 'for': 4, 'will': 5, 'learn': 5, 'it': 3, 
'build': 2, '—': 4, 'do': 3, 'a': 5, 'in': 2, 'way': 2, 'that': 2, 'people': 2, 
'me': 3, 'i': 7, 'have': 2, 'more': 2, 'programming': 2, 'this': 4, 'something': 2, 'be': 2, 
'or': 2, 'learning': 2, 'ive': 3, 'my': 2, 'new': 2, 'concepts': 2, 'coding': 3, 'go': 2}
:::