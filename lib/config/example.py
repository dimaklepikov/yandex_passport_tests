from config_parser import ConfigParser

parser = ConfigParser()

# RUN this script to test the value extraction from "config.ini" file
if __name__ == "__main__":
    parser.read()

    a = parser.config.sections()
    info = parser.get_section("Info")
    print("Get value by key 'version':")
    print(parser.get_value(info, "version"))
    print("Get value by key 'author':")
    print(parser.get_value(info, "author"))
