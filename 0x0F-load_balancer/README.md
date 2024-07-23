Sure, here's the content formatted in `.md` (Markdown) format:

---

# Double Web Servers and Configure Custom Nginx Header

## Task: Configure Custom Nginx Header

### Objective
Configure web-02 to match web-01, add a custom Nginx header, and automate setup with a Bash script.

### Requirements
- Configure Nginx on web-01 and web-02 to include a custom HTTP header:
  - **Header name:** `X-Served-By`
  - **Header value:** Hostname of the server (e.g., `web-01` or `web-02`)
- Create a Bash script (`0-custom_http_response_header`) to automate setup on a new Ubuntu machine.
- Note: Ignore SC2154 shellcheck warnings.

---

# Install and Configure HAProxy Load Balancer

## Task: Install and Configure HAProxy

### Objective
Install and configure HAProxy on lb-01 to distribute traffic to web-01 and web-02.

### Requirements
- Install HAProxy on lb-01.
- Configure HAProxy to:
  - Send traffic to web-01 and web-02.
  - Use the roundrobin algorithm for request distribution.
  - Ensure HAProxy can be managed via an init script.
- Verify servers have correct hostnames:
  - `[STUDENT_ID]-web-01`
  - `[STUDENT_ID]-web-02`
- Create a Bash script to automate setup on a new Ubuntu machine.

### Deliverable
A Bash script that configures a new Ubuntu machine to meet the above requirements.

---