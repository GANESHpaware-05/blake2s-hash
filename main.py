
import hashlib as hsl
from pyscript import document


def blake2s_converter(event):      
    pwd = document.getElementById('blake2s_input').value
    key = hsl.blake2s(pwd.encode('utf-8'))
    raja = key.hexdigest()
    print(raja)
    output_div = document.getElementById('blake2s_output')
    output_div.innerText = raja
