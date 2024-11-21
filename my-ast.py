import ast



# Exemple de code source
source_code = """
def addition(a, b):
    return a + b
"""

# Analyser le code source
tree = ast.parse(source_code)


print(ast.dump(tree, indent=4))
