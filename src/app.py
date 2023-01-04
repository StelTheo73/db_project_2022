from libraries.Windows import Window

if __name__=="__main__":
    print("@author: MyronG")
    print("@author: StelTheo73")
    print("Championship App")
    print("Starting GUI...")
    try:
        window = Window()
        window.mainloop()
    except KeyboardInterrupt:
        print("\n\nTerminating...")
        exit(0)