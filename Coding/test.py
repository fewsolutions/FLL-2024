import importlib

codesdict = {
    "A": ["RED", "code1"], 
    "B": ["BLUE", "code2"], 
    "C": ["GREEN", "code3"]
}

for key, value in codesdict.items():
    module_name = key
    code_name = value[1]
    module = importlib.import_module(module_name)
    globals()[code_name] = getattr(module, code_name)

# Now you can call code1, code2, and code3 directly
code1()
code2()
code3()