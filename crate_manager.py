"""
This file contains the main logic of the program - Crate Stash©
Crate Stash©, is a program for DJs that want to stash tracks that they hear & love
on a whim, and then later resort to that crate of stashed tracks to download
to their DJ playlist(s) for later use so they do not forget
"""

import json
from json import JSONDecodeError
from pathlib import Path

path = Path("data/crate.json")


class CrateManager:
    """Manage a crate of tracks for later download and DJ use."""

    def __init__(self):
        """Initialize variables."""


    def display_crate_stash_selection_menu(self):
        """Display a neatly formatted menu for the user."""
        print(f"\nWelcome to Crate Stash© - Stash & Go")
        print(
              "\n|   Crate Stash© Menu   |".center(35),  # Center text for neat.
              "\n1. Stash a track to crate"
              "\n2. Trash a track from crate"
              "\n3. View Crate Stash"
              "\n4. Quit"
        )

    def user_selection_menu_choice(self):
        """Return the user's menu choice in the form of an integer."""
        while True:
            try:
                choice = int(input("\nSelect a menu option (1-4): "))
            except ValueError:
                print("Please enter a valid number...")
                continue

            if choice < 1 or choice > 4:
                print("Invalid input! Please try again...")

            else:
                return choice

    def load_crate_stash_file(self):
        """
        Load crate stash data.
        If file does not exist or is invalid, create/reset.
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not found! Creating it now...")
            data = {}

            # Create the file and write empty JSON.
            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except JSONDecodeError as e:
            print(f"File is corrupt! Error at Line {e.lineno}, Column {e.colno}")

        else:
            return data

    def get_track_info(self):
        """Prompt user to enter info. about track and return values."""
        artist = input("\nEnter artist name: ").strip()
        title = input("Enter title of track: ").strip()

        track = {"artist": artist, "title": title}

        return track

    def save_track_to_crate(self, data):
        """(Add track) write data to .json file."""
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


    def remove_track_from_crate(self):
        """Remove track data from .json."""
        print("\nWhich track would you like to throwaway?")
        self.display_crate_stash()

    def display_crate_stash(self):
        """
        Print a neatly formatted display of stashed tracks within a crate.
        """
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for track in data["tracks"]:
            artist = track["artist"]
            title = track["title"]
            print(f"{artist} - {title}")

    def exit_crate_stash(self):
        """End the program."""

    def select_music_genre(self):
        """
        Prompt user to select a genre of music from the given list & return.
        """
        ...

    def run_crate_manager(self):
        """Orchestrator method."""
        while True:
            self.display_crate_stash_selection_menu()
            choice = self.user_selection_menu_choice()

            if choice == 1:
                data = self.load_crate_stash_file()

                if "tracks" not in data:
                    data["tracks"] = []

                new_track = self.get_track_info()
                data["tracks"].append(new_track)

                self.save_track_to_crate(data)
            elif choice == 2:
                self.load_crate_stash_file()
                self.remove_track_from_crate()
            elif choice == 3:
                self.display_crate_stash()
            else:
                self.exit_crate_stash()
                break





crate1 = CrateManager()

crate1.run_crate_manager()