import tkinter as tk
from tkinter import messagebox

def mad_libs():
    window = tk.Tk()
    window.title("Mad Libs Game")

    def submit():
        try:
            famous_person = famous_person_entry.get()
            adjective = adjective_entry.get()
            name_of_celebrity = name_of_celebrity_entry.get()
            number = int(number_entry.get())
            number2 = int(number2_entry.get())
            plant = plant_entry.get()
            name3 = name3_entry.get()
            verb = verb_entry.get()
            interjection = interjection_entry.get()
            song_title = song_title_entry.get()
            plural_animals = plural_animals_entry.get()

            result = (
                "Welcome to Florida Gulf Coast University. "
                "My name is {} and today I will be showing you around our campus. "
                "\nAt FGCU, we are blessed to have a {} campus. "
                "The school was founded in 1991 by {}. \nWe currently have {} students attending the university with "
                "{} living in student housing. Student housing is primarily divided into three areas: North Lake Village, "
                "West Lake Village, and South Village. "
                "Our campus is covered in many native Florida plants such as the {}. \nThe next stop on the tour is Howard Hall "
                "where you can talk to someone and learn more about undergraduate admissions. Right next door to Howard Hall is "
                "McTarnaghan Hall where you can talk to advisors regarding financial aid. "
                "\nAs we walk over here... {}! The shuttle is making its final stop. Quick, we have to {} if we are going to make it. "
                "One thing about our shuttles is the amazing drivers. Shuttle 32 is driven by {}. "
                "If you're listening on the shuttle, you can hear some of the top hits of the past decade such as: {}. "
                "\nAs we get off the shuttle, this concludes our tour of Florida Gulf Coast University. "
                "Thank you for joining me today, and as always, Go {}!".format(
                    famous_person, adjective, name_of_celebrity, number, number2, plant, interjection, verb, name3, song_title, plural_animals
                )
            )

            result_label.config(text=result)

        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid input.")

    tk.Label(window, text="Give the name of a famous person:").pack()
    famous_person_entry = tk.Entry(window)
    famous_person_entry.pack()

    tk.Label(window, text="Give an adjective:").pack()
    adjective_entry = tk.Entry(window)
    adjective_entry.pack()

    tk.Label(window, text="Give the name of a celebrity:").pack()
    name_of_celebrity_entry = tk.Entry(window)
    name_of_celebrity_entry.pack()

    tk.Label(window, text="Give a whole number:").pack()
    number_entry = tk.Entry(window)
    number_entry.pack()

    tk.Label(window, text="Give another whole number:").pack()
    number2_entry = tk.Entry(window)
    number2_entry.pack()

    tk.Label(window, text="Give a plant type:").pack()
    plant_entry = tk.Entry(window)
    plant_entry.pack()

    tk.Label(window, text="Give another name of a celebrity:").pack()
    name3_entry = tk.Entry(window)
    name3_entry.pack()

    tk.Label(window, text="Give an action word:").pack()
    verb_entry = tk.Entry(window)
    verb_entry.pack()

    tk.Label(window, text="Give an interjection:").pack()
    interjection_entry = tk.Entry(window)
    interjection_entry.pack()

    tk.Label(window, text="Give a song title:").pack()
    song_title_entry = tk.Entry(window)
    song_title_entry.pack()

    tk.Label(window, text="Give a plural form of an animal name:").pack()
    plural_animals_entry = tk.Entry(window)
    plural_animals_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()


mad_libs()
