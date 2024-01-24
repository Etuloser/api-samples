if __name__ == "__main__":
    import os
    from internal.videos.videos import Videos

    o = Videos()
    file = os.path.join("40adda3c.avi")
    print(o.upload_video(file))
