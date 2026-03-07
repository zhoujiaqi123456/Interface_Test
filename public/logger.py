'''
import logging
import os
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=10,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, delay=True, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)
    def get_log(self):
        return self.logger

    # def debug(self, msg):
    #     self.logger.debug(msg)
    #
    # def info(self, msg):
    #     self.logger.info(msg)
    #
    # def warning(self, msg):
    #     self.logger.warning(msg)
    #
    # def error(self, msg):
    #     self.logger.error(msg)
    #
    # def critical(self, msg):
    #     self.logger.critical(msg)

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "run.log")
log = Logger(log_dir, level='debug').get_log()
'''
import os

import logbook
from logbook.more import ColorizedStderrHandler

from conftest import ROOTDIR

log_dir = os.path.join(ROOTDIR, "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


def get_logger(name="SOP-", level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(ROOTDIR, "logs", '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


log = get_logger(level='INFO')
