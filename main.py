import requests

import wget

img_url = 'https://image.shutterstock.com/image-vector/vector-image-colorful-light-trails-260nw-1202405338.jpg'
video_url = 'https://v16-webapp.tiktok.com/69a4d096ce838e34472e19a977bfb51f/61e49eeb/video/tos/useast2a/tos-useast2a-ve-0068c001/659accb50ac94d70b71289a6cac050d1/?a=1988&br=1490&bt=745&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=XOQ9-3mYnz7ThPiQylXq&l=202201161640380102450401112499C970&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anZpbWQ6ZjQ5OjMzNzczM0ApODw3NztlNDtoN2Q3OmYzZ2diMi5qcjRfLl5gLS1kMTZzczAwYDVjLmFhL2IuYV4wYjU6Yw%3D%3D&vl=&vr='
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