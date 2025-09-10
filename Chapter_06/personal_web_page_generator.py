# Personal Web Page Generator

def main():
    name = input('Enter your name: ')
    description = input('Describe yourself: ')

    # Create the file.
    with open('my_page.html', 'w') as html_file:    
        # Write the HTML
        write_html(html_file, name, description)

def write_html(html_file, name, description):
    # Write the <html> tag.
    html_file.write('<html>\n')

    # Write the <head> element.
    write_head(html_file)

    # Write the body.
    write_body(html_file, name, description)

    # Write the </html> tag.
    html_file.write('</html>\n')

def write_head(html_file):
    html_file.write('<head>\n')
    html_file.write('<title>My Personal Web Page</title>\n')
    html_file.write('</head>\n')

def write_body(html_file, name, description):
    html_file.write('<body>\n')
    html_file.write('\t<center>\n')
    html_file.write('\t\t<h1>')
    html_file.write(name)
    html_file.write('</h1>\n')
    html_file.write('\t</center>\n')
    html_file.write('\t<hr />\n\t')
    html_file.write(description)
    html_file.write('\n\t<hr />\n')
    html_file.write('\t</body>\n')

if __name__ == '__main__':
    main()