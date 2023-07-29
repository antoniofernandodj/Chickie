from typing import List, Union, NoReturn
from os import getenv
import logging
import subprocess
from typing import Optional
import sys
import re

def get_error_number(string):
    pattern = re.compile(r"Found (\d+) error")
    match = pattern.search(string)
    if match:
        number = int(match.group(1))
        return number
    else:
        return 0

def init_app(args: list[str]) -> Union[None, NoReturn]:

    FILES = ['asgi.py']

    # args = sys.argv
    # args = [item.upper() for item in args]

    # if '--NO-CHECK' in args:
    #     logging.info(' * Skipping type-checking with mypy')
    #     return None
    
    # if 'NO-CHECK' in mode:
    #     logging.info(' * Skipping type-checking with mypy')
    #     return None
    args = [item.upper() for item in args]
    if '--CHECK-TYPES' in args or '-CT' in args:
        for FILE in FILES:
        
            params = ["mypy", FILE, "--check-untyped-defs"]
            logging.info(' * Checking application typing with untyped def with mypy')
            result = subprocess.run(params, capture_output=True)
            with open('mypy.log', 'wb') as logfile:
                logfile.write(result.stdout)
                
            stdout = result.stdout.decode('utf-8')
            logging.info(stdout)
            number_of_errors = get_error_number(stdout)
            if number_of_errors != 0:
                for linha in result.stdout.decode().split('\n'):
                    logging.info(linha)
                    
                sys.exit(-1)
            logging.info(
                ' * Checking application typing without untyped def with mypy'
            )  
            result = subprocess.run(params[:-1], capture_output=True)
            stdout = result.stdout.decode('utf-8')
            logging.info(stdout)
            if 'bodies of untyped functions are not checked' in stdout:
                with open('mypy.log', 'wb') as logfile:
                    logfile.write(result.stdout)
                for linha in result.stdout.decode().split('\n'):
                    logging.info(linha)
                    
                sys.exit(-1)
            
            if stdout:
                logging.info(f' * mypy: {stdout}')
