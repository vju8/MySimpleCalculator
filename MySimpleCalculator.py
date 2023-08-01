import tkinter as tk



class MyCalculator(): 
    
    def __init__(self):
        # establish the equation as an empty string, to which to concatenate later
        self.equation = ""
        self.result = ""
        
        
        # initializw window object
        self.root = tk.Tk()
        # set the title of the GUI window
        self.root.title("Simple Calculator")
        # set the geometry (+400+100 is the x- and y-axis shift when placing the GUI Window)
        self.root.geometry("550x540+400+100")
        # make the GUI window unresizable for both x- and y-axis
        self.root.resizable(False, False)
        
        # adjust the background color of the GUI Window to black
        self.root.configure(bg = "black")
        
        # create operation_label widget 
        self.operation_label = tk.Label(self.root, 
                                   width = 25, 
                                   height = 2, 
                                   text = "",
                                   font = ("Arial", 30),
                                   anchor = "e")
        self.operation_label.pack(fill = "x")      # position the operation_label at the top of GUI window
        
        # create the frame object needed to position the grid of calculator buttons
        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight = 1)
        buttonframe.columnconfigure(1, weight = 1)
        buttonframe.columnconfigure(2, weight = 1)
        buttonframe.columnconfigure(3, weight = 1)
        buttonframe.columnconfigure(4, weight = 1)
        
        tk.Button(buttonframe,text = "C", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#3697f5", command = lambda: self.clear()).grid(row = 0, column = 0, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "/", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("/")).grid(row = 0, column = 1, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "%", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("%")).grid(row = 0, column = 2, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "*", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("*")).grid(row = 0, column = 3, sticky = tk.W + tk.E + tk.S)
        # button row 2
        tk.Button(buttonframe,text = "7", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("7")).grid(row = 1, column = 0, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "8", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("8")).grid(row = 1, column = 1, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "9", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("9")).grid(row = 1, column = 2, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "-", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("-")).grid(row = 1, column = 3, sticky = tk.W + tk.E + tk.S)                                
        # button row 3                               
        tk.Button(buttonframe,text = "4", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("4")).grid(row = 2, column = 0, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "5", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("5")).grid(row = 2, column = 1, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "6", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("6")).grid(row = 2, column = 2, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "+", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("+")).grid(row = 2, column = 3, sticky = tk.W + tk.E + tk.S)                              
        # button row 4                      
        tk.Button(buttonframe,text = "1", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("1")).grid(row = 3, column = 0, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "2", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("2")).grid(row = 3, column = 1, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "3", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("3")).grid(row = 3, column = 2, sticky = tk.W + tk.E + tk.S)
        tk.Button(buttonframe,text = "=", width = 5, height = 3, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#fe9037", command = lambda: self.calculate()).grid(row = 3, column = 3, sticky = tk.W + tk.E + tk.S, rowspan=2)
        
        # button row 5        
        tk.Button(buttonframe,text = "0", width = 11, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show("0")).grid(row = 4, column = 0, sticky = tk.W + tk.E + tk.S, columnspan=2)                      
        tk.Button(buttonframe,text = ".", width = 5, height = 1, font = ("Arial", 30, "bold"), bd = 5, fg = "white", bg = "#2a2d36", command = lambda: self.show(".")).grid(row = 4, column = 2, sticky = tk.W + tk.E + tk.S)
        
        # position the buttonframe object
        buttonframe.pack(fill = tk.BOTH)
        
        # mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
        self.root.mainloop()
    
    def show(self, char):
        self.equation += char
        self.operation_label.config(text = self.equation)   
        
    def clear(self): 
        self.equation = ""
        self.operation_label.config(text = self.equation)    
        
    def calculate(self):
        try: 
            self.result = eval(self.equation)   # eval() method parses an expression (string) and runs its operation within program.
        except: 
            self.result = "ERROR"
        finally:
            self.equation = ""
        
        self.operation_label.config(text = self.result)
        
        
        
MyCalculator()