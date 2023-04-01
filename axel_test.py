
def format_string(str):
    tab_str = ""
    indent_num = 0;
    for c in str:
        if c == ':' or c == ',' or c == ';':
            if c == ':':
                indent_num += 1
                tab_str += '\n'
            elif c == ',':
                tab_str += '\n'
            elif c == ';':
                tab_str += '\n'
                indent_num -= 1
            for tab in range(indent_num):
                tab_str += '  '
        else:
            tab_str += c
        
    return tab_str


format_string("Service Info: Hosts: 127.0.1.1, UBUNTU, irc.TestIRC.net; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel")
