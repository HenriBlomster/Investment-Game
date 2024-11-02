import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import os

# Initialize pygame for playing audio
pygame.mixer.init()

# Define authorized users and valid answers
authorized_users = ["Henri", "Ernst", "Casper", "Monica", "Cappe", "Pavel"]
correct_answers = ["Asilo", "Asilo Argo", "Argo", "asilo", "asilo argo"]

# Define paths to the image and audio files
base_path = os.path.expanduser("~/Desktop/Game files")
winner_image_path = os.path.join(base_path, "Winner meme.jpg")  # Updated to .jpeg
loser_image_path = os.path.join(base_path, "Loser meme.png")    # Updated to .jpeg
victory_music_path = os.path.join(base_path, "Winner song.mp3")  # Updated to .mp3
loser_music_path = os.path.join(base_path, "Loser song.wav")     # Correct as .wav

# Function to display the winner screen
def show_winner():
    # Show the winner meme
    winner_img = Image.open(winner_image_path)
    # Resize the image to fit within 300x300 pixels
    winner_img.thumbnail((500, 800))
    winner_photo = ImageTk.PhotoImage(winner_img)
    result_label.config(image=winner_photo)
    result_label.image = winner_photo
    
    # Play victory music
    pygame.mixer.music.load(victory_music_path)
    pygame.mixer.music.play()

# Function to display the loser screen
def show_loser():
    # Show the loser meme
    loser_img = Image.open(loser_image_path)
    # Resize the image to fit within 300x300 pixels
    loser_img.thumbnail((500, 800))
    loser_photo = ImageTk.PhotoImage(loser_img)
    result_label.config(image=loser_photo)
    result_label.image = loser_photo
    
    # Play loser music
    pygame.mixer.music.load(loser_music_path)
    pygame.mixer.music.play()


# Function to check the player's answers
def check_authorization():
    first_name = name_entry.get()
    if first_name in authorized_users:
        ask_question()
    else:
        messagebox.showinfo("Access Denied", "Sorry, you are not authorized to play this game.")

# Function to ask the question about the best investment fund
def ask_question():
    # Ask the investment fund question
    answer = question_entry.get()
    if answer in correct_answers:
        show_winner()
    else:
        show_loser()

# Initialize main window
root = tk.Tk()
root.title("Simple Game")

# Set up the first question for the player's name
name_label = tk.Label(root, text="Enter your first name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Set up the second question for the investment fund
question_label = tk.Label(root, text="What is the best investment fund in the world?")
question_label.pack(pady=5)
question_entry = tk.Entry(root)
question_entry.pack(pady=5)

# Set up the button to start the game
start_button = tk.Button(root, text="Start Game", command=check_authorization)
start_button.pack(pady=10)

# Result label to display winner or loser meme
result_label = tk.Label(root)
result_label.pack(pady=10)

# Run the application
root.mainloop()
