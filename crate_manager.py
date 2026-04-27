"""
This file contains the main logic of the program - Crate Stash©
Crate Stash©, is a program for DJs that want to stash tracks that they hear & love
on a whim, and then later resort to that crate of stashed tracks to download
to their DJ playlist(s) for later use so they do not forget
"""


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

    def select_music_genre(self):
        """
        Prompt user to select a genre of music from the given list & return.
        """
        ...

    def add_track_to_crate(self):
        """Add a track data to .json."""


    def remove_track_from_crate(self):
        """Remove track data from .json."""


    def display_crate_stash(self):
        """
        Print a neatly formatted display of stashed tracks within a crate.
        """





crate1 = CrateManager()

crate1.display_crate_stash_selection_menu()
crate1.user_selection_menu_choice()