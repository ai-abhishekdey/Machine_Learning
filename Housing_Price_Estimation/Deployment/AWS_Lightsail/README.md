## Deployment in AWS Lightsail



1. Login to AWS Management Console as root user [Click Here](https://signin.aws.amazon.com/signin?client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_si%26src%3Dheader-signin%26state%3DhashArgsFromTB_eu-north-1_582b15ac24e32403&page=resolve&code_challenge=BuLK7FZTyPlT-uyFVlnxZEf6OB65aY8ksawowF3_G5E&code_challenge_method=SHA-256&backwards_compatible=true)


2. Search for **Lightsail**

<p align="left">
<img src="images/2.png" width="900" height="300">
</p>

3. Go to instances and click on **Create instance**

<p align="left">
<img src="images/3.png" width="900" height="300">
</p>

4. Select Linux/Unix platform and Ubuntu 24.04 LTS OS

<p align="left">
<img src="images/4.png" width="900" height="600">
</p>

5. Create SSH Key-pair, select a 2 GB memory system and create an instance

<p align="left">
<img src="images/5.png" width="900" height="600">
</p>

6. Ubuntu instance is created

<p align="left">
<img src="images/6.png" width="900" height="300">
</p>

7. Next go to **containers** and click on **create container service**

<p align="left">
<img src="images/7.png" width="900" height="300">
</p>

8. Choose **container service capacity**

<p align="left">
<img src="images/8.png" width="900" height="200">
</p>

9. Setup deployment

<p align="left">
<img src="images/9.png" width="900" height="600">
</p>

10. Setup public end point details

<p align="left">
<img src="images/10.png" width="900" height="600">
</p>

11. Create container service
<p align="left">
<img src="images/11.png" width="900" height="300">
</p>


12. Container service is **activated**. Click on the **Public domain** link to see the app running

<p align="left">
<img src="images/12.png" width="900" height="600">
</p>

13. To stop the container service, click on **Delete**

<p align="left">
<img src="images/13.png" width="900" height="600">
</p>

14. Don't forget to **Stop** and **Delete** the instance

<p align="left">
<img src="images/14.png" width="900" height="600">
</p>

