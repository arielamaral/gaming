#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Top 10 PlayStation 1 Games
Copyright (c) 2025 Ariel Amaral
Licensed under MIT License
"""

class Game:
    def __init__(self, title, developer, release_year, genre, description):
        self.title = title
        self.developer = developer
        self.release_year = release_year
        self.genre = genre
        self.description = description
    
    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.genre}"
    
    def display_details(self):
        """Print comprehensive details about the game."""
        print(f"\n{'=' * 50}")
        print(f"TITLE: {self.title}")
        print(f"DEVELOPER: {self.developer}")
        print(f"YEAR: {self.release_year}")
        print(f"GENRE: {self.genre}")
        print(f"{'=' * 50}")
        print(f"DESCRIPTION: {self.description}")
        print(f"{'=' * 50}\n")


def main():
    # Creating the top 10 PS1 games list
    top_ps1_games = [
        Game(
            "Final Fantasy VII",
            "Square",
            1997,
            "RPG",
            "A landmark JRPG following Cloud Strife and a group of eco-warriors "
            "as they fight against the Shinra Electric Power Company and the legendary "
            "soldier Sephiroth. Known for its emotional storytelling and iconic characters."
        ),
        Game(
            "Metal Gear Solid",
            "Konami",
            1998,
            "Stealth Action",
            "Directed by Hideo Kojima, this stealth-action game follows Solid Snake's "
            "infiltration of a nuclear weapons facility to neutralize a terrorist threat. "
            "Revolutionary for its cinematic presentation and complex narrative."
        ),
        Game(
            "Castlevania: Symphony of the Night",
            "Konami",
            1997,
            "Action RPG",
            "Alucard, son of Dracula, explores his father's castle in this seminal "
            "Metroidvania title. Features RPG elements, multiple endings, and a "
            "massive inverted castle that doubled the game's size."
        ),
        Game(
            "Resident Evil 2",
            "Capcom",
            1998,
            "Survival Horror",
            "Leon Kennedy and Claire Redfield fight to escape Raccoon City during "
            "a zombie outbreak. Improved upon the original with dual protagonists, "
            "each with unique storylines and encounters."
        ),
        Game(
            "Tony Hawk's Pro Skater 2",
            "Neversoft",
            2000,
            "Sports",
            "The definitive skateboarding game of its era, featuring a robust trick system, "
            "create-a-park mode, and an iconic soundtrack that defined a generation of gamers."
        ),
        Game(
            "Chrono Cross",
            "Square",
            1999,
            "RPG",
            "A spiritual successor to Chrono Trigger featuring a complex narrative involving "
            "parallel dimensions. Known for its unique battle system, massive cast of characters, "
            "and stunning soundtrack by Yasunori Mitsuda."
        ),
        Game(
            "Gran Turismo 2",
            "Polyphony Digital",
            1999,
            "Racing Simulation",
            "Featured over 600 cars and 27 tracks in this realistic driving simulator. "
            "The game's attention to detail and physics set the standard for racing games."
        ),
        Game(
            "Silent Hill",
            "Konami",
            1999,
            "Survival Horror",
            "Harry Mason searches for his missing daughter in the fog-shrouded town of Silent Hill. "
            "Known for its psychological horror, disturbing atmosphere, and multiple endings."
        ),
        Game(
            "Tekken 3",
            "Namco",
            1998,
            "Fighting",
            "Widely considered one of the greatest fighting games ever made, featuring refined 3D "
            "gameplay, a diverse roster of characters, and multiple game modes."
        ),
        Game(
            "Final Fantasy Tactics",
            "Square",
            1997,
            "Tactical RPG",
            "Set in the world of Ivalice, this deep tactical RPG tells a mature story of "
            "political intrigue, class warfare, and religious corruption. Features a complex "
            "job system and deep customization options."
        )
    ]
    
    # Display the list
    print("\nTOP 10 PLAYSTATION 1 GAMES OF ALL TIME\n")
    for index, game in enumerate(top_ps1_games, 1):
        print(f"{index}. {game}")
    
    # Option to display detailed information
    print("\nEnter a number from 1-10 to see more details about a game (or 0 to exit):")
    
    while True:
        try:
            choice = int(input("> "))
            if choice == 0:
                print("Goodbye!")
                break
            elif 1 <= choice <= 10:
                top_ps1_games[choice-1].display_details()
            else:
                print("Please enter a number between 1 and 10 (or 0 to exit).")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
