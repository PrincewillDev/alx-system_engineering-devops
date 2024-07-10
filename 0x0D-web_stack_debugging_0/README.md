# Debugging Docker Container with Apache

## Overview

In this project, you will debug a Docker container to get Apache running and returning a page containing "Hello Holberton" when querying the root of it.

## Prerequisites

Before starting, be sure to read the Docker concept page to familiarize yourself with the basic concepts and commands.

## Objective

Get Apache to run on the container and return a "Hello Holberton" page when querying the root.

## Steps

1. **Run the Docker Container**

    First, run the Docker container using the following command:

    ```bash
    docker run -p 8080:80 -d -it holbertonschool/265-0
    ```

    Example output:

    ```bash
    47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
    ```

2. **Check the Running Container**

    Verify that the container is running:

    ```bash
    docker ps
    ```

    Example output:

    ```bash
    CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
    47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
    ```

3. **Test the Server Response**

    Query the root of the server:

    ```bash
    curl 0:8080
    ```

    You might get an error message like:

    ```bash
    curl: (52) Empty reply from server
    ```

    This indicates that Apache is not returning the expected page.

4. **Fix the Issue**

    Connect to the Docker container:

    ```bash
    docker exec -it vigilant_tesla /bin/bash
    ```

    Inside the container, you need to diagnose and fix the issue with Apache. The goal is to ensure that querying port 80 returns a page with "Hello Holberton".

5. **Verify the Fix**

    After applying your fix, test again:

    ```bash
    curl 0:8080
    ```

    You should see:

    ```bash
    Hello Holberton
    ```

6. **Document the Fix**

    Paste the command(s) you used to fix the issue in your answer file.

## Example

Initial query returning an error:

```bash
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
```

After fixing the issue:

```bash
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
```
