from baby_yoda_bot.models import Context
from baby_yoda_bot.utils import print_not_found
from baby_yoda_bot.commands.commands import (
    CMD_CHANGE_NOTE,
    COMMAND_DESCRIPTION,
    ARG_CONTENT,
    ARG_TAGS,
    ARG_ID
)
from ..bot import Bot


@Bot.command(CMD_CHANGE_NOTE)
@Bot.description(COMMAND_DESCRIPTION[CMD_CHANGE_NOTE])
@Bot.questions(
    [
        {"name": ARG_ID , "required": True, "type": str},
        {"name": ARG_CONTENT , "optional": True, "type": str},
        {"name": ARG_TAGS , "optional": True, "type": str}
    ]
  
)
def change_note(ctx: Context, args):
    ARG_ID,ARG_CONTENT,ARG_TAGS = args
    note = ctx.notes.find_one(str(ARG_ID))
    if not note:
       return print_not_found(f'Con Note Id#"{ARG_ID}" not found.')
        
    if ARG_CONTENT:
        note.change_content(ARG_CONTENT)
        
    if ARG_TAGS.find(',')!=-1:
        tags = ARG_TAGS.split(",") 
        note.remove_tags()
        for tag in tags:
                note.add_tag(tag)       
    elif len(ARG_TAGS)>1 :
        note.remove_tags()
        note.add_tag(ARG_TAGS.strip())    

  
           
    return print(f'Note with Id#"{ARG_ID}" updated.') 
  


__all__ = ["change_note"]
