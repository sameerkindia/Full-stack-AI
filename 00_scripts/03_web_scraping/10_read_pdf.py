import pymupdf

def read_pdf(file_path):
    doc = pymupdf.open(file_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        all_text += page.get_text()

    doc.close()
    return all_text


if __name__ == "__main__":
    file_path = 'test.pdf'
    try:
        content = read_pdf(file_path)
        print('_' * 30)
        print(content)
        print('_' * 30)
    except Exception as e:
        print("Something went wrong " , e)