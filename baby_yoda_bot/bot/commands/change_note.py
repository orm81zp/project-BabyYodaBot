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
    id,content,teag_items = args
    note = ctx.notes.find_one(str(ARG_ID))
    if not note:
       return print_not_found(f'Con Note Id#"{id}" not found.')
        
    if content:
        note.change_content(content)
        
    if teag_items.find(',')!=-1:
        tags = teag_items.split(",") 
        note.remove_tags()
        for tag in tags:
                note.add_tag(tag)       
    elif len(teag_items)>1 :
        note.remove_tags()
        note.add_tag(teag_items.strip())    

  
           
    return print(f'Note with Id#"{id}" updated.') 
  


__all__ = ["change_note"]
