import requests

import wget

img_url = 'https://www.drifted.com/wp-content/uploads/2017/06/what-exactly-is-drifting.jpg'
video_url = ""
img2_wget = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/King_of_Europe_Round_3_Lydden_Hill_2014_%2814356011899%29.jpg/1200px-King_of_Europe_Round_3_Lydden_Hill_2014_%2814356011899%29.jpg'


def download_img(url = ''):
    try:
        response = requests.get(url = url)

        with open('req_img.jpg','wb') as file:
            file.write(response.content)
        
        return 'Img successfully downloaded'

    except Exception as _ex:
        return 'Uupss... check your URL again please its for vdeo'




def download_video(url = ''):
    try:
        response = requests.get(url = url, stream=True)

        with open('req_video.mp4','wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)


        return 'VIdeo successfully downloaded'

    except Exception as _ex:
        return 'Uupss... check your URL again please'

def download_wget(url = ''):
    wget.download(url=url )


def main():
    print(download_img(url = img_url))
    print(download_video(url = video_url))
    # download_wget(url = img2_wget)
if __name__ == '__main__':
    main()