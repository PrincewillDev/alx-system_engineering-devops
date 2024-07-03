# 0x0C. Web server

---

# 0. Transfer a File to Your Server

This Bash script (`0-transfer_file`) allows easy file transfer from a client to a server using `scp`.

## Requirements:

- Accepts 4 parameters:
  1. **PATH_TO_FILE:** File to transfer.
  2. **IP:** Server IP address.
  3. **USERNAME:** SSH username.
  4. **PATH_TO_SSH_KEY:** Path to SSH private key.

- Displays usage if parameters are insufficient:
  ```
  Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
  ```

- Transfers the file to the server's home directory (`~/`).

- Disables strict host key checking for seamless SSH connections.

## Example Usage:

1. **SSH into server to check home directory:**

   ```bash
   ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
   ```

2. **Create a file on client:**

   ```bash
   touch some_page.html
   ```

3. **Transfer file using script:**

   ```bash
   ./0-transfer_file some_page.html 8.8.8.8 ubuntu /vagrant/private_key
   ```

4. **Verify file transfer on server:**

   ```bash
   ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
   ```

## Conclusion

Use this script to securely transfer files between client and server via `scp` without manual intervention.

---
