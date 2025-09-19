# Working with Strings
from pyscript import display, document


def gettingstrings(e):
    #variables
    student = document.getElementById('name').value 
    age = document.getElementById('age').value
    school = document.getElementById('school').value
    
    #remove repeating to occur on display
    document.querySelector("#output").innerText = ""

    #multiline string
    msgoutcome = f"""Student Profile
    Name of Student: {student}
    Age of Student: {age}
    School and Campus: {school}

    Notes:
        \t{student}\'s age is {age}, and she goes to {school}. 
        The data being shown comes from the multiline string in python.
    """
    #displaying the message
    display(msgoutcome, target='output')