Project Description

The Airbnb Clone Project is a command-line interface (CLI) application designed to mimic the core functionalities of Airbnb. It allows users to manage listings, bookings, and user profiles through a terminal interface. This project is built with Python, utilizing the cmd module for the command interpreter and leveraging various Python libraries for data management and user interaction.
Command Interpreter Overview

The command interpreter is the heart of the Airbnb Clone Project, providing a user-friendly interface for managing Airbnb data. It is designed to be intuitive and powerful, allowing users to perform a wide range of operations without needing to interact with a graphical user interface.
How to Start It

To start the command interpreter, navigate to the root directory of the project in your terminal and run the following command:

python console.py

This command initializes the command interpreter, and you will be presented with a prompt where you can enter commands.
How to Use It

The command interpreter supports a variety of commands for managing listings, bookings, and user profiles. Here are some examples:

    Create a new user: create user <name> <email> <password>
    List all listings: list places
    Create a new listing: create place <name> <description> <price> <location>
    Book a listing: book <place_id> <start_date> <end_date>

Examples

Here are some examples of how to use the command interpreter

Creating a New User:

    create user John Doe john.doe@example.com password123

    Listing All Listings:

list places

    Creating a New Listing:

create place "Beach House" "A beautiful house by the beach." 100 "New York, NY"

    Booking a Listing:

book 1 2024-04-10 2024-04-17
