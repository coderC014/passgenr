# this is my module to generate random string 
# it provide the user to choose whether the string should contain how many letters, digits, punctuations

## this is how to use the module:

# Step1: Install module using pip
```bash
pip install passgenr
```
# Step2: create a file a follow this way to run,
```python
from passgenr import passgenr
# we need to import like this to avoid 'object not callable' error

## using my module
n_letter = 3
n_digit  = 4
n_symbol = 3
for i in range(10):
    myGen = passgenr.passgenr(n_letter, n_digit, n_symbol)
    print(myGen)
```
