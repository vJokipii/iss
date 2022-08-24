import classes

regions = ["Head", "Face", "Chest", "Abdomen", "Extremities", "External"]

print("\nISS SCORE CALCULATOR | INPUT VICTIM'S INJURIES \n\nINJURIES: No Injury, Minor, Moderate, Serious, Severe, Critical, Unsurvivable\n ")

def createprofile():
    arr = []

    for i in range(len(regions)):
        injury = input(f"{regions[i]} worst injury? ")
        br = classes.bodyregion(regions[i], injury)
        arr.append(br)
    return arr

array = createprofile()
body = classes.body(array)
print(f"Victim's ISS score is {body.calculatescore()}")