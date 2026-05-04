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
        print(f"\nWelcome to Crate Stash© - Stash & Go 💿")
        print(
              "\n|   Crate Stash© Menu   |".center(35),  # Center text for neat.
              "\n1. Stash a track to crate"
              "\n2. Trash a track from crate"
              "\n3. View Crate Stash"
              "\n4. Quit"
        )

    def selection_menu_choice(self):
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

    def save_crate_stash_file(self, data):
        """(Add track) write data to .json file."""
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_track_to_remove(self) -> int:
        """Prompts user to enter an integer, validates, and returns it."""
        while True:
            try:
                choice = int(input(
                    "\nWhich track would you like to trash 🗑?"
                    "\nEnter a corresponding number: "
                ))
            except ValueError:
                print("Please enter a valid number...")
                continue

            if choice <= 0:
                print("Invalid input! Please try again...")

            else:
                return choice

    def remove_track_from_crate(self, corresponding_track_num: int):
        """
        Load data, pop the selected track out of list in memory using the
        validated index, and save the updated data back to the JSON file.
        """
        data = self.load_crate_stash_file()

        track_index = corresponding_track_num - 1
        removed_track = data["tracks"].pop(track_index)

        self.save_crate_stash_file(data)

        print(f"\nTrashed🚮: {removed_track["artist"]} - {removed_track["title"]}")

    def display_crate_stash(self):
        """
        Print a neatly formatted display of stashed tracks within a crate.
        """
        print("\n--- Crate Stash© ---")

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        for number, track in enumerate(data["tracks"], start=1):
            artist = track["artist"]
            title = track["title"]
            print(f"{number}. {artist} - {title}")

    def exit_crate_stash(self):
        """End the program."""
        print(f"\nThanks for using Crate Stash©. Stash & Go 💿")

    def run_crate_manager(self):
        """Orchestrator method."""
        while True:
            self.display_crate_stash_selection_menu()
            choice = self.selection_menu_choice()

            if choice == 1:
                data = self.load_crate_stash_file()

                if "tracks" not in data:
                    data["tracks"] = []

                new_track = self.get_track_info()
                data["tracks"].append(new_track)

                self.save_crate_stash_file(data)

            elif choice == 2:
                self.load_crate_stash_file()
                self.display_crate_stash()
                corresponding_track_num = self.get_track_to_remove()
                self.remove_track_from_crate(corresponding_track_num)
            elif choice == 3:
                self.display_crate_stash()
            elif choice == 4:
                self.exit_crate_stash()
                break

crate1 = CrateManager()

crate1.run_crate_manager()