import webbrowser, sys
#webbrowser.open("https://www.google.co.in/search?client=ubuntu&channel=fs&q=how+to+clear+the+terminal+while+a+python+program+is+executing%3F&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=YX1IVZmyKePI8AeK7IHICw#channel=fs&q=how%20to%20execute%20python%20program%20in%20ubuntu")
if len(sys.argv) > 1:
    # Get address from command line.

 address = 'http://automatetheboringstuff.com/ '.join(sys.argv[1:])
#print address