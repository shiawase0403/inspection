def extract_and_format_text(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行首和行尾的空格
            line = line.strip()
            # 找到等号的位置
            equals_index = line.find('=')
            if equals_index != -1:
                # 提取等号前面的部分，并去除空格
                text_before_equals = line[:equals_index].strip()
                # 在前面加上“instance.”
                formatted_text = f"instance.{text_before_equals}"
                result.append(formatted_text)
    
    # 用加号连接所有的结果
    output = ' + '.join(result)
    return output

# 示例文件路径
file_path = 'D:/models.txt'

# 提取和格式化文本
formatted_output = extract_and_format_text(file_path)

# 打印结果
print(formatted_output)

