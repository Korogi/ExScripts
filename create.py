import os


def create_file(file_name):
    temp = open("template.txt", 'r').read()

    with open(f'{file_name}.java', 'w+') as f:
        f.write(temp.replace("$", file_name))


if __name__ == '__main__':
    classes = ["Composition", "Cosine", "Exponential", "Factor",
               "Identity", "Logarithm", "Power", "Product", "Reciprocal",
               "Sine", "Sum", "Tangent"]

    for class_name in classes:
        if not os.path.exists(f'{os.path.dirname(__file__)}/{class_name}.java'):
            create_file(class_name)
            print(f'{class_name} created.')
