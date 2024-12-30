# file= open("youtube.txt",'w')

# try:
#     file.write('Chai aur Code')
# finally:
#     file.close()

# with open('youtube.txt','w') as file:
#     file.write('Chai aur Python')

def list_all_videos():
    pass

while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List all youtube videos ")
    print("2. Add a youtube video")
    print("3. Update a youtube video details")
    print("4 . delete a youtube video")
    print("5. Exist the app ")
    choice = input("Enter your choice")
    
    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        