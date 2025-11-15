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
