from pynput import mouse
def on_click(x, y, button, pressed):
    print(x,y)
    # f=open("conaaf.txt","w+")
    # f.writelines(str(x))
    # f.writelines(str(y))
    # f.flush()
    # f.close()
    #listener.stop()
with mouse.Listener(on_click=on_click) as listener:
    listener.join()