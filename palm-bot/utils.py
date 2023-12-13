# --- 
# Description: 
#  Utils file for palm-bot project 
#  Contains the palm_bot class, which is used to query the palm api
#  for a response to a given prompt.
#  The prompt in question being: a discord message triggered by a
#  user command ('!palm <prompt>')
# 
# Contains tutorial code from: https://developers.generativeai.google/tutorials/text_quickstart
#
# Author:
#  Samuel Lemus
# --- 

import pprint 
import requests
import google.generativeai as palm 
from constants import generate_palm_constants

class palm_bot: 

    palm_token, palm_url = "", "" 
    model = "" 
    prompt = ""

    def __init__(self):

        self.palm_token, self.palm_url = generate_palm_constants()

        palm.configure(api_key=self.palm_token)

        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        self.model = models[0].name
        print(self.model)

        # test prompt run on init
        prompt = """
        You are an expert at solving word problems.

        Solve the following problem:

        I have three houses, each with three cats.
        each cat owns 4 mittens, and a hat. Each mitten was
        knit from 7m of yarn, each hat from 4m.
        How much yarn was needed to make all the items?

        Think about it step by step, and show your work.
        """

        completion = palm.generate_text(
            model=self.model,
            prompt=prompt,
            temperature=0,
            # The maximum length of the response
            max_output_tokens=800,
        )

        print(completion.result)

    def query_palm(message:str) -> str:
        print(message)
        if message == "":
            return "I'm sorry, I didn't catch that. Could you repeat yourself?"
        
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        completion = palm.generate_text(
            model=model,
            prompt=message,
            temperature=0,
            # The maximum length of the response
            max_output_tokens=800,
        )
        print(completion.result)
        return completion.result

