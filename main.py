# Coded By SpiderX

# Modules
from bs4 import BeautifulSoup
import requests
import tag_list


def SHOTGUN():
    print("""
     ,______________________________________       
    |_________________,----------._ [____]  ""-,__  __....-----=====
                   (_(||||||||||||)___________/   ""                |
                      `----------' SpiderX[ ))"-,                   |
                                           ""    `,  _,--....___    |
                                                   `/           ''''
    """)


# Getting Web URL


SHOTGUN()
print("Web Scraping Tool by Gigahertz Legacy- SpiderX")
print("\n")
print("Enter The url -- ex: https://facebook.com")
url = input("Enter the url : ")

# Getting Source Code

get_req = requests.get(url)

tag_list.ALL_TAGS()

while True:
    soup = BeautifulSoup(get_req.content, 'html.parser')
    try:
        user_input = int(input("Enter your Choice :"))
        print("\n")
        if user_input == 1:
            source = soup.prettify()
            print(source)

        elif user_input == 111:
            with open('html.txt', 'w') as HtmlFile:
                HtmlFile.write(content)
                HtmlFile.close()
        elif user_input == 999:
            print("Just Enter the tag name, ex: cite")
            custom_tag_input = input("Enter the tag :")
            cus_tag = soup.find_all(f'{custom_tag_input}')
            print(cus_tag)

        elif user_input == 2:
            a_tag = soup.find_all('a')
            print(a_tag)

        elif user_input == 4:
            img_tag = soup.find_all('img')
            print(img_tag)

        elif user_input == 3:
            anchors = soup.find_all('a')
            all_links = set()
            for links in anchors:
                if links.get('href') != "#":
                    links = f"{url}" + links.get('href')
                    all_links.add(links)
                    print(links)

        elif user_input == 5:
            p_tag = soup.find_all('p')
            print(p_tag)

        elif user_input == 6:
            bq_tag = soup.find_all('blockquote')
            print(bq_tag)

        elif user_input == 7:
            comment_tag = soup.find_all('!--')
            print(comment_tag)

        elif user_input == 8:
            table_tag = soup.find_all('table')
            print(table_tag)

        elif user_input == 9:
            ul_tag = soup.find_all('ul')
            print(ul_tag)

        elif user_input == 10:
            div_tag = soup.find_all('div')
            print(div_tag)

        elif user_input == 11:
            span_tag = soup.find_all('span')
            print(span_tag)

        elif user_input == 12:
            iframe_tag = soup.find_all('iframe')
            print(iframe_tag)

        elif user_input == 13:
            script_tag = soup.find_all('script')
            print(script_tag)

        elif user_input == 14:
            title_tag = soup.find_all('title')
            print(title_tag)

        elif user_input == 15:
            meta_tag = soup.find_all('meta')
            print(meta_tag)

        elif user_input == 16:
            code_tag = soup.find_all('code')
            print(code_tag)

        elif user_input == 17:
            section_tag = soup.find_all('section')
            print(section_tag)

        elif user_input == 18:
            body_tag = soup.find_all('body')
            print(body_tag)

        elif user_input == 19:
            canvas_tag = soup.find_all('canvas')
            print(canvas_tag)

        elif user_input == 20:
            svg_tag = soup.find_all('svg')
            print(svg_tag)

        elif user_input == 404:
            tag_list.ALL_TAGS()

        elif user_input == 909:
            exit()

        else:
            print("Type between the given integers---")

    except Exception as e:
        print(e)
