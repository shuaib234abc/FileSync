# FileSync

1. This is a small Python application that syncs some specified folders of one computer to another, remote computer.
2. The application has been made targeting Linux systems, and the rsync command has been used to sync files.
3. I wanted to sync some folders from my personal PC to a remote VPS every 10 seconds. Such a low sync frequency is not supported in cron jobs, so I decided to make this Python app.

Background:
My personal laptop has an Intel Atom processor with 2 GB RAM. It is not ideal for building applicatioons in Angular / .NET stack. So I use my personal laptop for code editing, and build the apps on a remote Linux VPS. I wanted something that would sync the code files on my personal PC with the code files on the VPS in close to real time.
