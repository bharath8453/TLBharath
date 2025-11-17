#day1 
Today I focused on setting up Terraform and Docker environments. While installing Terraform, I faced an issue where the command
winget install --id HashiCorp.Terraform -e

returned “No package found matching input criteria”, and winget itself wasn’t recognized in CMD. I solved this by manually downloading Terraform from the official HashiCorp site, unzipping it, and adding the path (C:\terraform) to the System Environment Variables. After that, running
terraform -version

successfully displayed the version output.
Next, I worked on Docker container creation but faced multiple issues. The command
docker run -it --rm --name add-app addition

gave the error:
python: can't open file '/usr/src/app/./telcopy': [Errno 2] No such file or directory

This occurred because the Dockerfile had incorrect working directory and copy paths. I fixed it by updating the file as follows:
FROM python:3.9
WORKDIR /usr/src/app
COPY . .
CMD ["python", "app.py"]

Then I rebuilt and ran the image using:
docker build -t addition .
docker run -it --rm --name add-app addition

I also learned that Docker requires WSL 2 to be enabled on Windows, which caused earlier setup problems (wsl --install not recognized). After enabling Windows Subsystem for Linux, Docker Desktop ran smoothly.
Overall, today’s challenges helped me understand environment configuration, path setup, Dockerfile structure, and Terraform CLI installation—key skills in DevOps automation.


#Day7


sbhar@Harshitha:/mnt/c/Users/sbhar$ mkdir -p ~/linux_practice/permissions
sbhar@Harshitha:/mnt/c/Users/sbhar$ cd ~/linux_practice
sbhar@Harshitha:~/linux_practice$ mkdir touch projects/app.py
mkdir: cannot create directory ‘projects/app.py’: No such file or directory
sbhar@Harshitha:~/linux_practice$ touch projects/app.py
touch: cannot touch 'projects/app.py': No such file or directory
sbhar@Harshitha:~/linux_practice$

2025-11-17T09:55:17.492687+00:00 Harshitha systemd-resolved[155]: Clock change detected. Flushing caches.
2025-11-17T09:55:45.468550+00:00 Harshitha wsl-pro-service[175]: #033[36mINFO#033[0m Daemon: connecting to Windows Agent
2025-11-17T09:55:45.469580+00:00 Harshitha wsl-pro-service[175]: #033[37mDEBUG#033[0m Updated systemd status to "Connecting"
2025-11-17T09:55:45.470837+00:00 Harshitha wsl-pro-service[175]: #033[33mWARNING#033[0m Daemon: could not connect to Windows Agent: could not get address: could not read agent port file "/mnt/c/Users/sbhar/.ubuntupro/.address": open /mnt/c/Users/sbhar/.ubuntupro/.address: no such file or directory
2025-11-17T09:55:45.471014+00:00 Harshitha wsl-pro-service[175]: #033[36mINFO#033[0m Reconnecting to Windows host in 60 seconds
2025-11-17T09:55:45.471091+00:00 Harshitha wsl-pro-service[175]: #033[37mDEBUG#033[0m Updated systemd status to "Not connected: waiting to retry"
2025-11-17T09:55:49.091895+00:00 Harshitha systemd-resolved[155]: Clock change detected. Flushing caches.
