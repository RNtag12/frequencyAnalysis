# FrequencyAnalysis
# Project Description
This project aims to analyze the frequency of letters in a given message and compare it to the typical frequency of letters in the English language. By determining the frequency order of letters in the message, it can help identify how closely a text matches standard English letter distribution. This is particularly useful in cryptography for tasks such as breaking substitution ciphers. Note that this code is based on a code from "Cracking Codes with Python" by Al Sweigart (BSD Licensed).

# Features
- <b>Letter Frequency Count</b>: Counts the frequency of each letter in a given message.
- <b>Frequency Order Calculation</b>: Determines the order of letters based on their frequency in the message.
- <b>English Frequency Match Score</b>: Calculates how well the letter frequency of the message matches the expected frequency of English letters.
Simple and readable Python code.

# Code Explanation
The solution involves several functions:
- <b>getLetterCount(message)</b>: Counts the occurrence of each letter in the message.
  - Returns a dictionary with keys of single letters 
  - Returns values of the count of how many times they appear in the message parameter
- <b>getFrequencyOrder(message)</b>: Determines the frequency order of letters in the message.
  - Returns Returns a string of the alphabet letters arranged in order of most frequently occurring in the message parameter
- <b>englishFreqMatchScore(message)</b>: Compares the frequency of letters in the message to typical English letter frequency and calculates a match score.
  - Return the number of matches that the string in the message parameter has when its letter frequency is compared to English letter frequency

# Interactions in the Code
- <b>Letter Count</b>: The getLetterCount function creates a dictionary with letters as keys and their counts as values, based on the input message.
- <b>Frequency Order</b>: The getFrequencyOrder function creates an ordered string of letters based on their frequency in the input message.
- <b>Match Score</b>: The englishFreqMatchScore function calculates how closely the letter frequency of the input message matches typical English letter frequency.

# Steps to Execute the Project
Prepare the Environment: Ensure Python is installed on your system. Create a new directory for the project and navigate to it.
Create the Script: Copy the provided code into a Python script file (e.g., frequency_finder.py).
Run the Script: Execute the script by importing it into your Python environment and using the functions with your desired message.
Review the Output: Use the functions to analyze letter frequencies and match scores for different messages.
This project is a useful tool for understanding letter frequencies in texts, which can be applied in cryptography and language analysis.
