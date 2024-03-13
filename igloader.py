import instaloader

L = instaloader.Instaloader()


loader = instaloader.Instaloader()

# Login (optional)
# loader.interactive_login("your_username")

# Target username
target_username = ['iceskycoldly']


# Download all posts

for item in target_username:
    loader.download_profile(item, profile_pic_only=False)

    