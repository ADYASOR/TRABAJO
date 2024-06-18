
#1 upper(): convierte todas las letras de una cadena a mayúsculas.

text= "hello world"
print(text.upper())
#HELLO WORLD

#2 lower(): convierte todas las letras de una cadena a minúsculas.

text = "HELLO WORLD"
print(text.lower())
# hello world

#3 strip(): elimina los espacios en blanco al principio y al final de una cadena.

text = "   hello world   "
print(text.strip())
# hello world

#4 replace(old, new): reemplaza todas las ocurrencias de una subcadena con una nueva subcadena.

text = "hello world"
print(text.replace("world", "python"))
# hello python

#5 split(sep): divide una cadena en una lista de subcadenas usando un separador dado.

text = "hello,world,python"
print(text.split(","))
# ['hello', 'world', 'python']

#6 join(iterable): une una lista de cadenas en una única cadena usando la cadena actual como separador.

words = ["hello", "world", "python"]
text = " ".join(words)
print(text)
# hello world python

#7 len(string): devuelve la longitud de una cadena, es decir, el número de caracteres en la cadena.

text = "hello world"
print(len(text))
# 11

#8 startswith(prefix): devuelve True si una cadena comienza con un prefijo dado, de lo contrario devuelve False.

text = "hello world"
print(text.startswith("hello"))
# True

#9 endswith(suffix): devuelve True si una cadena termina con un sufijo dado, de lo contrario devuelve False.

text = "hello world"
print(text.endswith("world"))
# True


#10 find(substring): devuelve el índice de la primera aparición de una subcadena en una cadena, o -1 si la subcadena no se encuentra en la cadena.

text = "hello world"
print(text.find("world"))
# 6

#11 index(substring): funciona de manera similar a find, pero en su lugar lanza una excepción ValueError si la subcadena no se encuentra en la cadena.

text = "hello world"
print(text.index("world"))
# 6

#12 count(substring): devuelve el número de ocurrencias de una subcadena en una cadena.

text = "hello world, world"
print(text.count("world"))
# 2
  
#13 format(): permite insertar valores dinámicos en una cadena.

name = "John"
age = 30
text = "My name is {} and I am {} years old.".format(name, age)
print(text)
# My name is John and I am 30 years old.

#14 isdigit(): devuelve True si una cadena contiene solo dígitos y False en caso contrario.
 
 text = "12345"
print(text.isdigit())
# True

#15 isalpha(): devuelve True si una cadena contiene solo letras y False en caso contrario.

text = "hello"
print(text.isalpha())
# Output: True

#16 isalnum(): devuelve True si una cadena contiene solo letras y dígitos y False en caso contrario.

text = "hello123"
print(text.isalnum())
# True

# 17 istitle(): devuelve True si una cadena está en formato de título, es decir, si cada palabra comienza con una mayúscula y las demás letras son minúsculas, y False en caso contrario.

text = "Hello World"
print(text.istitle())
# True
