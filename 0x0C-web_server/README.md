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


Here's a README file based on your provided task:

---

# Free .TECH Domain Setup Guide

.TECH Domains is one of the top domain providers, known for their stability and quality of DNS hosting solutions. We have partnered with .TECH Domains so that you can learn about DNS. Follow these steps to get your free .TECH domain for 1 year.

## Steps to Get Your Free .TECH Domain

1. **Access the Tools Space:**
   Unlock the GitHub student pack. **WARNING:** This invitation link is unique to you and can’t be reclaimed! If you have any issues, please contact GitHub education support.

2. **Register Your Domain:**
   - Access your benefits after registering.
   - Scroll to the .TECH domain section.
   - Start the registration process and proceed to checkout.

3. **Login with GitHub:**
   At the checkout step, please click on “Login with GitHub”. The cost of the domain should now be $0.

4. **Finalize Registration:**
   Create an account with .TECH Domains and manage your domain there.

## Requirements

1. **Domain Name:**
   - Provide the domain name only (example: `foobar.tech`), no subdomains (example: `www.foobar.tech`).

2. **Configure DNS Records:**
   - Set an A record so that your root domain points to your `web-01` IP address.
   - Note: The propagation of your records can take time (~1-2 hours).

3. **Update Your Profile:**
   - Go to your profile and enter your domain in the Project website URL field.

## Example

```sh
# Register your domain (example: foobar.tech)

# Configure DNS A record
# Example: 
# A record for foobar.tech pointing to your web-01 IP address

# Update your profile
# Enter foobar.tech in the Project website URL field
```

---

This README should provide clear instructions for obtaining and setting up a free .TECH domain, as well as configuring DNS records and updating the project URL.

3-redirection - This script configures Nginx server so that file /redirect_me is redirecting to another page.


# Free .TECH Domain Setup Guide

.TECH Domains is one of the top domain providers, known for their stability and quality of DNS hosting solutions. We have partnered with .TECH Domains so that you can learn about DNS. Follow these steps to get your free .TECH domain for 1 year.

## Steps to Get Your Free .TECH Domain

1. **Access the Tools Space:**
   Unlock the GitHub student pack. **WARNING:** This invitation link is unique to you and can’t be reclaimed! If you have any issues, please contact GitHub education support.

2. **Register Your Domain:**
   - Access your benefits after registering.
   - Scroll to the .TECH domain section.
   - Start the registration process and proceed to checkout.

3. **Login with GitHub:**
   At the checkout step, please click on “Login with GitHub”. The cost of the domain should now be $0.

4. **Finalize Registration:**
   Create an account with .TECH Domains and manage your domain there.

## Requirements

1. **Domain Name:**
   - Provide the domain name only (example: `foobar.tech`), no subdomains (example: `www.foobar.tech`).

2. **Configure DNS Records:**
   - Set an A record so that your root domain points to your `web-01` IP address.
   - Note: The propagation of your records can take time (~1-2 hours).

3. **Update Your Profile:**
   - Go to your profile and enter your domain in the Project website URL field.

## Example

```sh
# Register your domain (example: foobar.tech)

# Configure DNS A record
# Example: 
# A record for foobar.tech pointing to your web-01 IP address

# Update your profile
# Enter foobar.tech in the Project website URL field
```

---

This README should provide clear instructions for obtaining and setting up a free .TECH domain, as well as configuring DNS records and updating the project URL.


### 3-redirection

This script configures the Nginx server to redirect the file `/redirect_me` to another page.

### 4-not_found_page_404

This script configures the Nginx server to have a custom 404 page that displays the message "Ceci n'est pas une page".


