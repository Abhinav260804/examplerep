from jinja2 import Template
data=[{"year":1965,"awardees":"abhinav","language":"telugu"},{"year":1965,"awardees":"abhinav","language":"telugu"},{"year":1965,"awardees":"abhinav","language":"telugu"}]


def main():

    temp_file=open('/Users/abhi/Documents/mad1/week3/awardees.html.jinja2')
    TEMPLATE=temp_file.read()
    temp_file.close()

    template=Template(TEMPLATE)
    content=template.render(data=data)

    awardees_file=open('awardees.html','w')
    awardees_file.write(content)
    awardees_file.close()

if __name__=="__main__":
    main()