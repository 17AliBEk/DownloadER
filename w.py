import wget

img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/King_of_Europe_Round_3_Lydden_Hill_2014_%2814356011899%29.jpg/1200px-King_of_Europe_Round_3_Lydden_Hill_2014_%2814356011899%29.jpg'
def download(url = ''):
    wget.download(url = url, out = 'image.jpg')

def main():
    download(url = img_url)

if __name__ == '__main__':
    main()