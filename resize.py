from PIL import Image

for i in range(1, 6574):
    base_width = 60
    img = Image.open(f'frames/{i:0>4}.png')
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    img.save(f'frames/{i:0>4}.png')
    print(i)