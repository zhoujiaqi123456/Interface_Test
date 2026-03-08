# -*- coding:utf-8 -*-
"""
中文转拼音工具
使用 pypinyin 将中文转换成拼音
"""
import re
from pypinyin import lazy_pinyin, Style
from typing import Optional


class Translator:
    """中英文转换器"""
    
    def __init__(self):
        """初始化"""
        self._cache = {}  # 缓存翻译结果
    
    def to_pinyin(self, text, style='normal'):
        """
        中文转拼音
        :param text: 中文文本
        :param style: 转换风格
            - 'normal': 默认，不带声调
            - 'camel': 驼峰命名
            - 'snake': 蛇形命名
        :return: 转换后的文本
        """
        if not text:
            return text
        
        # 检查是否包含中文
        if not self._contains_chinese(text):
            # 不包含中文，直接返回原文本
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
    
    def _contains_chinese(self, text: str) -> bool:
        """检查是否包含中文"""
        return any('\u4e00' <= char <= '\u9fa5' for char in text)
    
    def translate_filename(self, text: str) -> str:
        """
        翻译文件名（转拼音，下划线命名）
        :param text: 文件名（中文或英文）
        :return: 拼音文件名（下划线命名）
        """
        if not text:
            return text
        
        # 移除特殊字符（保留中文、英文、数字、下划线、连字符）
        text = re.sub(r'[^\w\u4e00-\u9fa5-]', '_', text)
        
        # 转为拼音（小写蛇形命名）
        return self._to_snake_case(text).lower()
    
    def translate_class_name(self, text: str) -> str:
        """
        翻译类名（转拼音，帕斯卡命名）
        :param text: 类名（中文或英文）
        :return: 拼音类名（帕斯卡命名）
        """
        if not text:
            return text
        
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 转为拼音（帕斯卡命名）
        return self._to_pascal_case(text)
    
    def translate_method_name(self, text: str) -> str:
        """
        翻译方法名（转拼音，蛇形命名）
        :param text: 方法名（中文或英文）
        :return: 拼音方法名（蛇形命名）
        """
        if not text:
            return text
        
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 转为拼音（蛇形命名）
        return self._to_snake_case(text)
    
    def translate_description(self, text: str) -> str:
        """
        翻译接口描述（转拼音，蛇形命名）
        :param text: 接口描述（中文或英文）
        :return: 拼音描述（蛇形命名）
        """
        if not text:
            return text
        
        # 转为拼音（小写蛇形命名）
        return self._to_snake_case(text).lower()
    
    def _to_snake_case(self, text: str) -> str:
        """转蛇形命名"""
        # 先转拼音
        pinyin_text = self.to_pinyin(text, style='snake')
        
        # 替换空格和连字符为下划线
        pinyin_text = pinyin_text.replace('-', '_').replace(' ', '_')
        
        # 处理驼峰命名
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', pinyin_text)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
        
        # 转小写并移除多余下划线
        result = s2.lower()
        result = re.sub(r'_+', '_', result)
        result = result.strip('_')
        
        return result
    
    def _to_pascal_case(self, text: str) -> str:
        """转帕斯卡命名"""
        # 先转蛇形
        snake = self._to_snake_case(text)
        # 再转帕斯卡
        words = snake.split('_')
        return ''.join(word.capitalize() for word in words if word)


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
    
    print("\n=== 描述翻译 ===")
    print(f"登录接口 -> {translator.translate_description('登录接口')}")
    print(f"根据ID获取用户信息 -> {translator.translate_description('根据ID获取用户信息')}")
