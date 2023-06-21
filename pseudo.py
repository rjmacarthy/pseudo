import openai
import yaml
import sys
from rich.console import Console
from rich.markdown import Markdown

config = yaml.safe_load(open("config.yaml"))
model = config["model_engine"]
console = Console()


def get_completion(messages):
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )


def start_sudo_session():
    sudo_lang = open("sudolang-llm-support/sudolang.sudo.md", "r").read()
    if not sudo_lang:
        console.print("Error: Could not load sudolang.")
        return
    messages = [{"role": "system", "content": sudo_lang}]
    return messages


def get_sudo_program(file_path):
    with open(file_path, "r") as file:
        return file.read()


def start(program_name):
    console.print(f"running {program_name} using pseudo version 1.0 🚀 Enter `/help` for help or `/start` run the program.")
    while True:
        user_input = input(">: ")
        if user_input == "/start":
            load(program_name)
        else:
            console.print("Welcome to pseudo! Enter `/start` to run the program.")
            continue
    

def load(program_name):
        console.print(f"Loading {program_name}... please wait.")
        messages = start_sudo_session()
        program = get_sudo_program(program_name)
        messages.append({"role": "user", "content": program})
        completion = get_completion(messages)
        reply = completion["choices"][0]["message"]["content"]
        console.print(reply)
        while True:
            user_input = input(">: ")

            if user_input == "/restart":
                start(program_name)

            if user_input == "/quit":
                break

            if user_input == "/help":
                console.print(
                    Markdown("Enter `/help` to see this message, `/quit` to quit and `/restart` to restart.")
                )
            messages.append({"role": "user", "content": user_input})
            completion = get_completion(messages)
            reply = completion["choices"][0]["message"]["content"]
            console.print(reply)
            continue
            
def main():
    if len(sys.argv) < 2:
        console.print("Please enter a program name to run e.g `pseudo folder/program.sudo`")
        return
    start(sys.argv[1])
    