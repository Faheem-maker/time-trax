# Time Trax

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faheem_Anis-green)](https://www.linkedin.com/in/faheem-anis)
<br>
![GitHub contributors](https://img.shields.io/github/contributors/Faheem-maker/time-trax)
![GitHub forks](https://img.shields.io/github/forks/Faheem-maker/time-trax)
![GitHub followers](https://img.shields.io/github/followers/Faheem-maker)
![GitHub Repo stars](https://img.shields.io/github/stars/Faheem-maker/time-trax)
![Static Badge](https://img.shields.io/badge/license-MIT-orange)
![GitHub issues](https://img.shields.io/github/issues-raw/Faheem-maker/time-trax)

## Time Trax Repoistory
Welcome to time trax, it is a Python based time tracker that runs every regularly logs your input and stores them in Google Sheets for use later.<br>
The code may seem a little crude, and the application itself will not seem very helpful. It is meant for users who need  to actively log their time in a highly customizable and convenient way.

## Table of Contents

- [Time Trax](#time-trax)
  - [Time Trax Repoistory](#time-trax-repoistory)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Techstack](#techstack)
  - [Setup](#setup)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Time trax was created as a 3 hour project, where I attempted to create something to streamline my Google Sheets time logging. I created an application that will run every 30 minutes to get my input on what am I doing and will place it in a highly customized Google Spreadsheet that I personalized as much as possible.

I am hoping to spend some more time and transform the project into something convenient that everyone can use If you like the project, please show your support by adding a star or making a small contribution, and I would spend more time on this project.

## Techstack

The following technologies are used:

- Python
- Tkinter (For GUI)
- Google Sheets (Data Storage)
- Windows Task Scheduler (For auto startup)

## Setup

Please follow the following steps to install and run the project:

- Make sure you have Python installed.
- Run <code>pip install -r requirements.txt</code> to install the required dependencies.
- Create a new Google service account on developer console, download the credentials and save them as <code>credentials.json</code> in the same directory.
- Upload the provided sheet (<code>Time_Tracking_Worksheet.xlsx</code>) to Google Sheets and share it with your service account.
- Copy the sheet ID from your spreadsheet URL and place it in the <code>.env</code> file.
- Use the command <code>python refresh_categories.py</code> to download the categories you added to your template and <code>python tracker.py</code> to launch a GUI program where you can input your current tasks.
- (OPTIONAL) Setup the task scheduler to run the file every 30 minutes

## Contributing

Feel free to contribute to this repository by adding new scripts or improving existing ones. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

Please adhere to the [Contributing Guidelines](CONTRIBUTING.md).

## License

This repository is licensed under the [MIT License](LICENSE), allowing you to use the code for both personal and commercial projects.

Happy coding!
