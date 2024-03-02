import time, mouse, keyboard, clipboard
from get_tetr_string import get_tetr
from PIL import Image
import PIL.ImageGrab

def main():
    time.sleep(5)
    for i in range(101, 501):
        print(i)
        if i > 1 and get_tetr(i-1) == get_tetr(i):
            im = Image.open(f'output/{i-1:0>4}.png')
            im.save(f'output/{i:0>4}.png')
        else:
            time.sleep(1)
            mouse.move(1000, 600)
            mouse.click()
            time.sleep(0.2)
            mouse.click()
            clipboard.copy(get_tetr(i))
            time.sleep(2)
            mouse.move(1000, 500)
            mouse.click()
            time.sleep(0.1)
            keyboard.press_and_release('ctrl+a, backspace, ctrl+v')
            mouse.move(1500, 300)
            mouse.click()
            time.sleep(2)
            mouse.move(0, 0)
            im = PIL.ImageGrab.grab()
            im.save(f'output/{i:0>4}.png')
            keyboard.press('esc')
            time.sleep(1.1)
            keyboard.release('esc')

if __name__ == '__main__':
    main()