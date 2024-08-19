# Web Stack Debugging #4 - Optimizing Nginx Server Performance

## Project Overview

In this project, we are tasked with identifying and resolving performance issues in a web server setup featuring Nginx. The server is under heavy load, and a significant number of HTTP requests are failing during benchmarking tests. Our goal is to analyze the server's configuration, identify the root cause of the failures, and implement a solution to reduce the number of failed requests to zero.

## Tools and Environment

- **Operating System**: Ubuntu 14.04 LTS
- **Web Server**: Nginx
- **Benchmarking Tool**: ApacheBench
- **Puppet Version**: 3.4
- **puppet-lint Version**: 2.1.1

## Task Requirements

### General
- All files must be interpreted on Ubuntu 14.04 LTS.
- Each file should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must:
  - Pass `puppet-lint` version 2.1.1 without any errors.
  - Run without errors.
  - Include a comment on the first line explaining the purpose of the manifest.
  - End with the `.pp` file extension.
- All files will be checked with Puppet version 3.4.

#### Description:
In this web stack debugging task, we are testing the performance of our Nginx server under heavy load. Using ApacheBench, we simulate 2000 HTTP requests to the server, with 100 requests being made simultaneously. However, 943 of these requests have failed, indicating that our current server configuration cannot handle the load efficiently.

#### Objective:
- Analyze the Nginx server setup to identify performance bottlenecks.
- Optimize the server configuration to handle the load more effectively.
- Reduce the number of failed requests to zero.
