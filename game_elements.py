import os
import re
from cmd_color_printer import ColorPrinter, print_hat
from work_place import *
from mine import Mine
from school import School
from company import Company
from person import Person
from teacher import Teacher
from engineer import Engineer
from worker import Worker
import random


class GameElements:
    # below can be customized, and in future I will use json
    # the ability to set game elements by user will be implemented soon

    # in future I will use a complete english names json and it will get more diverse
    first_names:list[str] = [  
        "Sophia", "Jackson", "Olivia", "Aiden", "Emma", "Lucas",  
        "Ava", "Elijah", "Isabella", "James", "Mia", "Liam",  
        "Amelia", "Noah", "Harper", "Oliver", "Evelyn", "Ethan",  
        "Abigail", "Mason", "Charlotte", "Logan", "Ella"  
    ]  

    last_names:list[str] = [  
        "Smith", "Johnson", "Williams", "Jones", "Brown",  
        "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez",  
        "Anderson", "Taylor", "Thomas", "Hernandez", "Moore",  
        "Martin", "Jackson", "Thompson", "White", "Lopez"  
    ]
    ages: list[int] = [i for i in range(18,60)]

    # Lists of sample attributes, nouns, and abbreviations for  creating companies name
    adjectives = [  
        "Global", "Innovative", "Dynamic", "Synergy", "Green",   
        "Smart", "NextGen", "Creative", "Premium", "Advanced"  
    ]  

    nouns = [  
        "Solutions", "Group", "Technologies", "Systems", "Enterprises",  
        "Industries", "Services", "Concepts", "Partners", "Consultants",  
        "Networks", "Developers", "Designs", "Investments", "Resources",  
    ]  

    abbreviations = [  
        "LLC", "Inc", "Corp", "Co", "PLC", "Solutions",  
        "NGO", "LKO", "Partners", "GmbH", "SAS"  
    ]  
    @staticmethod
    def generate_random_company_name():  
        # Randomly choose an adjective, a noun, and an abbreviation  
        adjective = random.choice(GameElements.adjectives)  
        noun = random.choice(GameElements.nouns)  
        abbreviation = random.choice(GameElements.abbreviations)  
        
        # Format the company name with or without an abbreviation  
        if random.choice([True, False]):  
            return f"{adjective} {abbreviation}"  
        else:  
            return f"{adjective} {noun}"
        
    @staticmethod
    def generate_random_name() -> str:  
        first_name = random.choice(GameElements.first_names)
        last_name = random.choice(GameElements.last_names)
        return f"{first_name} {last_name}" 
    
    @staticmethod
    def generate_random_age() -> int:  
        return random.choice(GameElements.ages)
    
    def __init__(self) -> None:
        self.__work_places: list[WorkPlace] = []
        self.__people: list[Person] = []
        self.__round:int = 0
        list1 = [1, 2, 3]
        for _ in range(2000):
            if random.choice(list1)==1:
                self.__people.append(Teacher(GameElements.generate_random_name(),GameElements.generate_random_age()))
            elif random.choice(list1)==2:
                self.__people.append(Worker(GameElements.generate_random_name(),GameElements.generate_random_age()))
            elif random.choice(list1)==3:
                self.__people.append(Engineer(GameElements.generate_random_name(),GameElements.generate_random_age()))

        for _ in range(200):
            if random.choice(list1)==1:
                self.__work_places.append(Company(GameElements.generate_random_company_name()))
            elif random.choice(list1)==2:
                self.__work_places.append(School(GameElements.generate_random_company_name()))
            elif random.choice(list1)==3:
                self.__work_places.append(Mine(GameElements.generate_random_company_name()))


    def __str__(self) -> str:  
        printer = ColorPrinter()  
        workers_list:list[str] = []
        places_list:list[str] = []

        # Print game round  
        workers_list.append(f"{printer.colors['blue']}Round: {self.__round}{printer.colors['reset']}\n")  

        # Print People  
        workers_list.append(f"{printer.colors['yellow']}People in the game:{printer.colors['reset']}\n")  
        for person in self.__people:  
            workers_list.append(f" - {printer.colors['cyan']}{str(person)}{printer.colors['reset']}")  
        workers_list = " <-///-> ".join(workers_list)
        # Print Workplaces  
        places_list.append(f"\n{printer.colors['yellow']}Workplaces in the game:{printer.colors['reset']}\n")  
        for work_place in self.__work_places:  
            places_list.append(f" - {printer.colors['magenta']}{str(work_place)}{printer.colors['reset']}")  
        places_list = " <-///-> ".join(places_list)
        output = [workers_list,places_list]  
        return "\n".join(output)