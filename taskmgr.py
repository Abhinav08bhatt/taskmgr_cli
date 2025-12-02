import os # checking the file path and clearing the terminal
import argparse # main structure to take terminal command to variables
import json # data format
import sys # for analyzing the terminal command

# File for the data:
DATA_FILE = "taskdata.json"

# =========================== FUNCTIONS ===========================
# prints the variable from the terminal commands
def TerminalCmdInfo():
    print(sys.argv)

def load_data():
    if not os.path.exists(DATA_FILE):
        return "NO DATA YET!"
    with open(DATA_FILE,"r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data,f,indent=4)


# =========================== ARGPARSE ============================
description_text = '''
Task manager for you that can add, remove update and mark 

version    : 1.0

add        : adds new task to list
                - python taskmgr.py add "title"
                - python taskmgr.py add "title" --mark "mark"
update     : updates name of an existing task
                - python taskmgr.py update task_id "new_title"
delete     : deletes an existing task
                - python taskmgr.py delete task_id
list       : shows all the tasks
                - python taskmgr.py list
                - python taskmgr.py list --filter "mark"
'''
cmd = argparse.ArgumentParser(description=description_text,formatter_class=argparse.RawDescriptionHelpFormatter)
subcmd = cmd.add_subparsers(dest="command")

#    ======================== commands ========================

#                ============== add ==============
add_cmd = subcmd.add_parser("add",help="python taskmgr.py add 'title' --mark 'mark'")
#                   ======== arguments ========
add_cmd.add_argument("title",type = str,help = "a new task (string)")
add_cmd.add_argument(
    "--m","--mark",
    choices = ["todo","done","in-progress"],
    default = "todo",
    help = "default : todo"
)

#               ============== update ==============
update_cmd = subcmd.add_parser("update",help="python taskmgr.py update task_id 'new_title'")
#                   ========= arguments ========
update_cmd.add_argument("task_id",type = int,help = "task number (int)")
update_cmd.add_argument("new_title",type = str,help = "a new task name (string)")

#               ============== update ==============
delete_cmd = subcmd.add_parser("delete",help="python taskmgr.py delete task_id")
#                   ========= arguments ========
delete_cmd.add_argument("task_id",type = int,help = "task number (int)")

#               ============== list ==============
list_cmd = subcmd.add_parser("list",help="python taskmgr.py list --filter 'mark'")
#                  ========= arguments ========
list_cmd.add_argument(
    "-f","--filter",
    choices = ["todo","done","in-progress"],
    help = "shows all the tasks"
)

#  ======================== Finalizing ========================
args = cmd.parse_args()