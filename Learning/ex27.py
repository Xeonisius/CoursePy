import sys
from xml.etree.ElementTree import XMLParser

class CubeValueCalculator:
    def __init__(self):
        self.red_value = 0
        self.green_value = 0
        self.blue_value = 0
        self.depth = 0
    
    def start(self, tag, attrib):
        self.depth += 1
        color = attrib.get('color')
        if color == 'red':
            self.red_value += self.depth
        elif color == 'green':
            self.green_value += self.depth
        elif color == 'blue':
            self.blue_value += self.depth
    
    def end(self, tag):
        self.depth -= 1
    
    def data(self, data):
        pass
    
    def get_values(self):
        return self.red_value, self.green_value, self.blue_value

def main():
    input_data = sys.stdin.read().strip()
    
    target = CubeValueCalculator()
    parser = XMLParser(target=target)
    parser.feed(input_data)
    red_value, green_value, blue_value = target.get_values()
    print(red_value, green_value, blue_value)

if __name__ == "__main__":
    main()