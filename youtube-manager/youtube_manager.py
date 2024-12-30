import json

mainFileName = "youtube.txt"

def load_data():
    try:
        with open(mainFileName, 'r') as file:
            content = json.load(file)
            print(content)
            print(type(content))
            if not content:  # Handle empty file
                return []
            return content  # Parse JSON
    except FileNotFoundError:
        print("No existing data found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Corrupt data found. Resetting the file.")
        return []
def save_data_helper(videos):
    with open(mainFileName, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    else:
        print("\nList of Videos:")
        for index,video in enumerate(videos,start=1):
            print("*"*50)
            print(f"{index}. Video Name: {video['name']} , Duration: {video['time']} \n")
            
def add_video(videos):
    
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print(f"Video '{name}' added successfully!")

def update_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name=input("Enter ye new video name :")
        time=input("Enter the new video time : ")
        videos[index-1]={"name":name,"time":time}
        save_data_helper(videos)
    else:
        print("invalid user index")
     
def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
