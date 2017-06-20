#!usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os
import sys
# import huodong_mysql

level_none = logging.NOTSET
level_debug = logging.DEBUG
level_info = logging.INFO
level_warn = logging.WARN
level_error = logging.ERROR
level_critical = logging.CRITICAL

class Common_logger(object):
    def __init__(self,s_name_log,filter_name,s_path_log="E:\\Python-project\\Selenium\\ggcj\\huodong",
                 i_level_log=logging.DEBUG):

        self.commonLogger = logging.getLogger(s_name_log)

        # 此处必须要给commonLogger对象进行设置日志级别，否则下边handler设置日志级别无效
        self.commonLogger.setLevel(i_level_log)

        fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')
        fh = logging.FileHandler(os.path.join(s_path_log,s_name_log))
        sh = logging.StreamHandler()
        ft = logging.Filter(filter_name)

        fh.setFormatter(fmt)
        sh.setFormatter(fmt)

        fh.setLevel(level_info)
        sh.setLevel(level_warn)
        sh.addFilter(ft)

        self.commonLogger.addHandler(fh)
        self.commonLogger.addHandler(sh)
        self.commonLogger.addFilter(ft)

    def debug(self,s_message_log):
        # print ("this is debug_log")
        self.commonLogger.debug(s_message_log)

    def info(self,s_message_log):
        # print ("this is info_log")
        self.commonLogger.info(s_message_log)

    def warning(self,s_message_log):
        self.commonLogger.warning(s_message_log)

    def error(self,s_message_log):
        self.commonLogger.error(s_message_log)

    def critical(self,s_message_log):
        self.commonLogger.critical(s_message_log)

class TestLogging(object):

    def __init__(self):
        self.logger = Common_logger(self.__class__.__name__,self.__class__.__name__,i_level_log=logging.DEBUG)

    def testFunc(self):
        # print (self.__class__.__name__,sys._getframe().f_code.co_name)
        self.logger.info('[%s.%s]:I test info'%(self.__class__.__name__, sys._getframe().f_code.co_name))
        self.logger.debug('[%s.%s]:I test debug'%(self.__class__.__name__, sys._getframe().f_code.co_name))
        self.logger.error('[%s.%s]:I test error'%(self.__class__.__name__, sys._getframe().f_code.co_name))
        self.logger.warning('[%s.%s]:I test warning' % (self.__class__.__name__, sys._getframe().f_code.co_name))
        self.logger.critical('[%s.%s]:I test critical' % (self.__class__.__name__, sys._getframe().f_code.co_name))

#
# def print_log_level(info="This is info message!"):
#     # config_logging()
#
#     logging.debug('This is debug message!')
#     logging.info(info)
#     logging.warning("This is a warning message!")
#     logging.error("This ia a error message!")
#     logging.critical("This is a critical message!")
#     print ("critical > error > warning > info > debug > notset")
#
# def config_logging():
#     logging.basicConfig(level = logging.DEBUG,
#                         format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                         datefmt = '%Y,%m,%d,%a  %H:%M:%S',
#                         filename='huodong.log',
#                         filemode='w')
# print_log_level()

if __name__=="__main__":
#     # print_log_level()
#     # config_logging()
    log = TestLogging()
    log.testFunc()