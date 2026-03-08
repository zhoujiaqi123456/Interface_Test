# -*- coding:utf-8 -*-
"""
中文转拼音工具
用于将中文文件名、类名、方法名转换为英文拼音
"""
from pypinyin import lazy_pinyin, Style
import re


class Translator:
    """中英文转换器"""
    
    @staticmethod
    def to_pinyin(text, style='normal'):
        """
        中文转拼音（不带声调）
        :param text: 中文文本
        :param style: 转换风格
            - 'normal': 默认，不带声调
            - 'camel': 驼峰命名
            - 'snake': 蛇形命名
        :return: 转换后的文本
        """
        if not text:
            return text
        
        # 使用拼音转换（不带声调）
        pinyin_list = lazy_pinyin(text, style=Style.NORMAL)
        
        if style == 'camel':
            # 驼峰命名
            return ''.join(word.capitalize() for word in pinyin_list if word)
        elif style == 'snake':
            # 蛇形命名
            return '_'.join(word for word in pinyin_list if word)
        else:
            # 默认：直接连接
            return ''.join(word for word in pinyin_list if word)
    
    @staticmethod
    def to_camel_case(text):
        """转驼峰命名"""
        # 先转蛇形
        snake = Translator.to_pinyin(text, style='snake')
        # 再转驼峰
        return Translator._snake_to_camel(snake)
    
    @staticmethod
    def to_snake_case(text):
        """转蛇形命名"""
        return Translator.to_pinyin(text, style='snake')
    
    @staticmethod
    def to_lower_snake_case(text):
        """转小写蛇形命名"""
        return Translator.to_snake_case(text).lower()
    
    @staticmethod
    def _snake_to_camel(name):
        """蛇形命名转驼峰命名"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    @staticmethod
    def translate_filename(text):
        """
        翻译文件名
        :param text: 文件名（中文或英文）
        :return: 英文文件名
        """
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 检查是否包含中文
        if any('\u4e00' <= char <= '\u9fa5' for char in text):
            # 转为拼音（小写蛇形）
            return Translator.to_lower_snake_case(text)
        else:
            # 已经是英文，转蛇形
            return Translator._snake_to_camel(text)
    
    @staticmethod
    def translate_class_name(text):
        """
        翻译类名
        :param text: 类名（中文或英文）
        :return: 英文类名
        """
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 检查是否包含中文
        if any('\u4e00' <= char <= '\u9fa5' for char in text):
            # 转为驼峰命名
            return Translator.to_camel_case(text)
        else:
            # 已经是英文，转驼峰
            return Translator._to_camel_from_snake(text)
    
    @staticmethod
    def _to_camel_from_snake(name):
        """蛇形命名转驼峰命名"""
        words = name.replace('-', '_').replace(' ', '_').split('_')
        return ''.join(word.capitalize() for word in words if word)
    
    @staticmethod
    def translate_method_name(text):
        """
        翻译方法名
        :param text: 方法名（中文或英文）
        :return: 英文方法名（蛇形命名）
        """
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 检查是否包含中文
        if any('\u4e00' <= char <= '\u9fa5' for char in text):
            # 转为蛇形命名
            return Translator.to_lower_snake_case(text)
        else:
            # 已经是英文，转蛇形
            return Translator._snake_to_camel(text)


if __name__ == '__main__':
    # 测试
    translator = Translator()
    
    print("=== 文件名翻译 ===")
    print(f"账号相关 -> {translator.translate_filename('账号相关')}")
    print(f"设备控制 -> {translator.translate_filename('设备控制')}")
    print(f"轻量化肺功能 -> {translator.translate_filename('轻量化肺功能')}")
    
    print("\n=== 类名翻译 ===")
    print(f"账号相关 -> {translator.translate_class_name('账号相关')}")
    print(f"设备控制 -> {translator.translate_class_name('设备控制')}")
    
    print("\n=== 方法名翻译 ===")
    print(f"登录 -> {translator.translate_method_name('登录')}")
    print(f"获取用户信息 -> {translator.translate_method_name('获取用户信息')}")
