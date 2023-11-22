from xml.etree import ElementTree as ET


class ProcessingXML:
    def __init__(self):
        self.root = None

    def load_xml_from_string(self, xml_string):  # Метод для завантаження XML з стр.
        try:
            self.root = ET.fromstring(xml_string)
            return True
        except ET.ParseError as e:
            print(f"Помилка при розборі XML: {e}")
            return False

    def convert_to_string(self):  # Метод для конвертації XML в стрингу.
        if self.root is not None:
            return ET.tostring(self.root).decode()
        else:
            print("XML не був завантажений.")
            return None

    def add_new_element(self):  # Метод для виконання операцій з xml.etree.додамо елемент NewElement
        if self.root is not None:
            new_element = ET.Element("NewElement")
            new_element.text = "HELLO"
            self.root.append(new_element)
            print("Новий елемент додано")
        else:
            print("XML не був завантажений.")


xml_string = '<root><element1>Value1</element1><element2>Value2</element2></root>'

process = ProcessingXML()
process.load_xml_from_string(xml_string)

process.add_new_element()

xml_new_to_str = process.convert_to_string()
if xml_new_to_str:
    print(xml_new_to_str)

# Конвертуємо XML в строку
xml_as_string = process.convert_to_string()
if xml_as_string:
    print(f"Конвертація в строку:\n{xml_as_string}")




