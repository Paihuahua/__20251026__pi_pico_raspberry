from machine import Timer


#timer = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))


def callback2000(n):
    global count
    count += 1
    if count == 5:
        n.deinit()
        print("再見")
    else:
        print("hello pico")
        
        
def main():
    timer = Timer(period = 2000, callback = callback2000)
    
if __name__ =="__main__":
    count = 0
    main()
        
        

    
    