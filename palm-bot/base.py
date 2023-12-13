# --- 
# Description: 
#  Base file for palm-bot project
#  Contains the base classes used by the palm-bot project
#  This file contains remnants of a tutorial I found about a year ago. 
# If im able to find the original author, I will credit them 
# Not all of this code is mine. 
# 
# --- 

from dataclasses import dataclass 
from typing import List, Optional 

SEPARATOR_TOKEN = "<|endoftext|>"

@dataclass(frozen=True) 
class Message: 
    user: str 
    text: Optional[str] = None

    def render(self) -> str: 
        result = self.user + ":"
        if self.text: 
            result += self.text
        return result
    
@dataclass
class Conversation: 
    messages: List[Message] = None

    def prepend(self, message: Message) -> None: 
        self.messages.insert(0, message)
    
    def render(self) -> str:
        return SEPARATOR_TOKEN.join(
            [message.render() for message in self.messages]
            )

@dataclass(frozen=True)
class Config: 
    name: str
    instructions: str 
    example_conversations: List[Conversation]

@dataclass(frozen=True)
class Prompt: 
    header: Message
    examples: List[Conversation] 
    convo: Conversation 

    def render(self) -> str:
        return f"\n{SEPARATOR_TOKEN}".join(
            [self.header.render()]
            + [Message("System", "Example conversations:").render()]
            + [conversation.render() for conversation in self.examples]
            + [Message("System", "Current conversation:").render()]
            + [self.convo.render()],
        )