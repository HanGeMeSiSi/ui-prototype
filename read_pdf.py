import pdfplumber

def read_pdf(file_path):
    try:
        # 打开PDF文件
        with pdfplumber.open(file_path) as pdf:
            # 获取PDF页数
            num_pages = len(pdf.pages)
            print(f"PDF总页数: {num_pages}")
            
            # 读取每一页的内容
            for page_num in range(num_pages):
                page = pdf.pages[page_num]
                text = page.extract_text()
                print(f"\n第 {page_num + 1} 页内容:")
                print("-" * 50)
                print(text)
                
    except Exception as e:
        print(f"读取PDF时发生错误: {str(e)}")

if __name__ == "__main__":
    pdf_path = "易智拍面部智能速拍仪产品介绍.pdf"
    read_pdf(pdf_path) 