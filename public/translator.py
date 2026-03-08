# -*- coding:utf-8 -*-
"""
中文转英文工具
使用 googletrans 将中文翻译成英文
"""
import re
from googletrans import Translator as GoogleTranslator
from typing import Optional


class Translator:
    """中英文转换器"""
    
    def __init__(self):
        """初始化 Google 翻译器"""
        self.translator = GoogleTranslator()
        # 缓存翻译结果，避免重复翻译
        self._cache = {}
    
    def to_english(self, text: str) -> str:
        """
        中文转英文
        :param text: 中文文本
        :return: 英文文本
        """
        if not text:
            return text
        
        # 检查缓存
        if text in self._cache:
            return self._cache[text]
        
        # 检查是否包含中文
        if not self._contains_chinese(text):
            # 不包含中文，直接返回
            self._cache[text] = text
            return text
        
        try:
            # 翻译成英文（使用 zh-cn 作为源语言）
            result = self.translator.translate(text, src='zh-cn', dest='en')
            translated = result.text
            self._cache[text] = translated
            return translated
        except Exception as e:
            print(f"翻译失败: {text}, 错误: {e}")
            # 翻译失败，返回原文
            return text
    
    def _contains_chinese(self, text: str) -> bool:
        """检查是否包含中文"""
        return any('\u4e00' <= char <= '\u9fa5' for char in text)
    
    def translate_filename(self, text: str) -> str:
        """
        翻译文件名（下划线命名）
        :param text: 文件名（中文或英文）
        :return: 英文文件名（下划线命名）
        """
        if not text:
            return text
        
        # 移除特殊字符（保留中文、英文、数字、下划线、连字符）
        text = re.sub(r'[^\w\u4e00-\u9fa5-]', '_', text)
        
        # 翻译成英文
        english = self.to_english(text)
        
        # 转为下划线命名（小写）
        return self._to_snake_case(english)
    
    def translate_class_name(self, text: str) -> str:
        """
        翻译类名（帕斯卡命名）
        :param text: 类名（中文或英文）
        :return: 英文类名（帕斯卡命名）
        """
        if not text:
            return text
        
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 翻译成英文
        english = self.to_english(text)
        
        # 转为帕斯卡命名
        return self._to_pascal_case(english)
    
    def translate_method_name(self, text: str) -> str:
        """
        翻译方法名（蛇形命名）
        :param text: 方法名（中文或英文）
        :return: 英文方法名（蛇形命名）
        """
        if not text:
            return text
        
        # 移除特殊字符
        text = re.sub(r'[^\w\u4e00-\u9fa5]', '_', text)
        
        # 翻译成英文
        english = self.to_english(text)
        
        # 转为蛇形命名
        return self._to_snake_case(english)
    
    def translate_description(self, text: str) -> str:
        """
        翻译接口描述（小写蛇形命名）
        :param text: 接口描述（中文或英文）
        :return: 英文描述（小写蛇形命名）
        """
        if not text:
            return text
        
        # 翻译成英文
        english = self.to_english(text)
        
        # 转为小写蛇形命名
        return self._to_snake_case(english)
    
    def _to_snake_case(self, text: str) -> str:
        """转蛇形命名（小写）"""
        # 替换空格和连字符为下划线
        text = text.replace('-', '_').replace(' ', '_')
        
        # 处理驼峰命名
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
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
