from PIL import Image

file_names = [r'\file1.jpg', r'\file2.jpg', r'\file3.jpg', r'\file4.jpg']
root_dir = r"C:\Users\karol\Desktop\Python_zajecia"

paths = []

for name in file_names:
    paths.append(root_dir + name)

for path in paths:
    image_open = Image.open(path)
    image_open.save(path.replace('.jpg', '_png.png'))
