import tiktoken

def count_token(input_file):
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    # UTF8エンコードのテキストファイルの読み込み
    with open(input_file, encoding='utf-8') as f:
        text = f.read()

    # for doc in documents:
    #     text += doc.page_content.replace("\n", " ")
    token_count = len(encoding.encode(text, allowed_special='all'))
    print(f"トークン数: {token_count}")
    print(f"予想価格: {token_count*0.00000004} USD")
    
if __name__ == "__main__":
    count_token("tmp.txt")