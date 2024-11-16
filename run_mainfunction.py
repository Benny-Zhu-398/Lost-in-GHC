import tkinter as tk
from cmu_graphics import *

def onAppStart(app):
    app.colorMatrix = []
    app.path_4 = []
    app.path_5 = []
    app.CLASSROOM = []
    app.currPoint = None
    app.destination = None
    getinput(app)
    app.directions = [(0,1), (0,-1), (1,0), (-1,0), (-1,1), (1,1), (-1,-1), (1,-1)]
    app.elevator = 4800

def getinput(app):
    root = tk.Tk()
    root.title("Location Input")
    root.geometry("400x300")

    # Define variables to store input
    currPoint = tk.StringVar()
    destPoint = tk.StringVar()

    # Label and Entry for Current Location
    currLabel = tk.Label(root, text="Current Location:")
    currLabel.pack(pady=10)
    currTextBox = tk.Entry(root, textvariable=currPoint, width=30)
    currTextBox.pack(pady=10)

    # Label and Entry for Destination Location
    destLabel = tk.Label(root, text="Destination Location:")
    destLabel.pack(pady=10)
    destTextBox = tk.Entry(root, textvariable=destPoint, width=30)
    destTextBox.pack(pady=10)

    # Submit Button
    submitButton = tk.Button(root, text="Submit", command=submitLocations)
    submitButton.pack(pady=20)

    # Label to show the result
    resultLabel = tk.Label(root, text="", justify="center")
    resultLabel.pack(pady=10)
    # run the code
    root.mainloop()

# Define the button click event
def submitLocations(app):
    app.currPoint = currPoint.get()  # Get the current location input
    app.destination = destPoint.get()  # Get the destination location input
    print(f"Current Location: {app.currPoint}")
    print(f"Destination Location: {app.destination}")
    # Here you can store the inputs into variables or pass them to other parts of your program
    resultLabel.config(text=f"Current: {app.currPoint}\nDestination: {app.destination}")
 

def getColorMatrix(app):
    # we got a image
    image1 =
    # we divide the image into small images

    for i in range(rows):
        for j in range(cols):
    # check the colormap for 4th floor
    # call classify_cell to define the cell
    # so we got the matrix for 4th floor

    #same procedure for 5th floor
    image2 =
    # we divide the image into small images

    for i in range(rows):
        for j in range(cols):
    # check the colormap for 4th floor
    # call classify_cell to define the cell
    # so we got the matrix for 4th floor

def getPath(app):
    # we get the starting point and destination
    # we use starting point and destination as an input for backtracking, the color matrix from getColorMatrix should be the input of the get path
    # we got the path list. contains the position tuple of the path
    if app.startingpoint and app.destination:
        currPoint = app.CLASSROOM[app.currPoint]
        target = app.CLASSROOM[app.destination]
        app.path = navigatePath(app,currPoint,target)

def navigatePath(app, currPoint, target):
    currFloor = app.currPoint//1000
    targetFloor = target//1000
    toElevator = False
    newTarget = None
    if(currFloor != targetFloor):
        #guide to elevator
        toElevator = True
        # this means the elevator's position
        newTarget = app.elevator
        elevator_row,elevator_col = app.CLASSROOM[app.elevator]

    row, col = currPoint
    if toElevator:
        if currFloor == 4:
            app.path_4 = helper(app, row, col, set(), newTarget, toElevator)
            app.path_5 = helper(app, elevator_row, elevator_col, set(), target, toElevator)
        else:
            app.path_5 = helper(app, row, col, set(), newTarget, toElevator)
            app.path_4 = helper(app, elevator_row, elevator_col, set(), target, toElevator)
    else:
        if currFloor == 4:
            app.path_4 = helper(app, row, col, set(), target, toElevator)
        else:
            app.path_5 = helper(app, row, col, set(), target, toElevator)

def helper(app, row, col, visited, target, toElevator):
    rows, cols = len(app.colorMatrix), len(app.colorMatrix[0])
    # Diagonal moves
    if(row, col) == target:
        return True
    else:
        for (dRow, dCol) in app.directions:
            for i in range(len(app.colorMatrix)):
                newR = row + dRow*i
                newC = col + dCol*i
                if(isLegal(app, newR, newC, row, col, visited)):
                    visited.add((newR,newC))
                    possible = helper(app.colorMatrix, newR, newC, visited, target, toElevator)
                    if(possible != False):
                        toElevator = not toElevator
                        return True
                newR -= dRow*i
                newC -= dCol*i 
        return False

def isLegal(app, newR, newC, row, col, visited):
    if((newR>=0 and newR<len(app.colorMatrix)) and 
        (newC>=0 and newC<len(app.colorMatrix)) and 
        app.colorMatrix[newR][newC] == 2 and (newR, newC) not in visited):
        return True
    return False

def reDrawAll(app):
    #draw map(first we need to decide which floor we need to draw based on the input)
    #draw path(for row and col in the past list set the cell to be blue)
    #if mousepress is within some classroom, highlight it.

