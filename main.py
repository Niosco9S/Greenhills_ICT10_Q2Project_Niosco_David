#Ict project meet the creator
from pyscript import document

# Information about the creator, indexed by button name
Creator = {
    'About Me': 'Name: David Niosco<br> Grade & Section: Grade 10 - Sapphire <br> Favorite Subject: ICT',
    'Interests': 'Coding <br> Science <br> Music',
    'Hobbies': 'Playing video games <br><br> Reading',
    'Dreams': 'To live a happy and successful life <br>',
    'Favorite Quote': '"I think, Therefore I am." <br> - Rene Baterbonia Descartes'
}
#displays the information of the button that was clicked
def show_info(event):
    topic = event.target.innerText
    results = document.getElementById('results')
    results.innerHTML = Creator.get(topic, 'Click one of the buttons above.') #if the button is not in the dictionary