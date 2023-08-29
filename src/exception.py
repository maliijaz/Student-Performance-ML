import sys
import logger
import logging

def error_message_detail(error, error_detail:sys):
    excinfodata = error_detail.exc_info()
    exc_tb = excinfodata[2]
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = "Error: {} \nFile: {} \nLine No: {}".format(str(error), file_name, line_no)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail) 
    def __str__(self):
        return self.error_message 
    



