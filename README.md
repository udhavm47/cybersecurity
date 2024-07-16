# These are my projects and practices related to cybersecurity 

Clone the repository and do the following

## HTBs:
- Once you have cloned the repo you can use cherry a note taking application comes pre installed with kali linux to see all the walkthroughs
## Python Projects
### Instructions Port scanner
- Install the requirements using pip command
   ```bash
    pip3 install -r requirements.txt
- Usage
  after installing the requirements, navigate to the directory and type the following command
  ```bash
        python3 nmapscanner.py <Your-target-name>

- Output
  
  ![Screenshot from 2024-07-15 22-50-32](https://github.com/user-attachments/assets/ec1d86e6-ac11-4458-b44a-52d135a5eba1)
### Instructions TCP Socket
- Usage
     on server side
     ```bash
        python3 Server.py
     ```
     ![Screenshot from 2024-07-16 21-14-27](https://github.com/user-attachments/assets/0423ccb9-07c7-40b0-a3c2-3e38c92e8ff1)


     on client side
     ```bash
        python3 Client.py <target-IP>
     ```
     ![Screenshot from 2024-07-16 21-15-49](https://github.com/user-attachments/assets/066dd78e-4f02-40a2-8bc1-e3fdb811452a)

  after the connection is established you will see something like this
  
  ![Screenshot from 2024-07-16 21-17-32](https://github.com/user-attachments/assets/b8ed4b83-05d3-4c2f-a779-346c1895299c)
  
  "$" represents you , and ":" represents the sender's message 
