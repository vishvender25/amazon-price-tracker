
# Amazon product price tracker
This python script monitors the current price of a product at amazon and sends you an alert message once the price reaches a target value.



## Authors

- [@vishvender tyagi](https://www.github.com/vishvender25)


## Appendix

#### How to use?
the script requires a url of the product that needs to be tracked. You need to provide the url and the price of that product will be monitored frequently using web scrapping.

#### libraries used
The project uses smtplib to send the alert email when the price reaches the target value.  
The project uses the beautifulsoap library from the bs4 to scrap the website to fetch the current price of the target value.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

these are the environment variavble that will be used in the script to send you an alert message.     

`MY_PASS`   

`MY_EMAIL`


## Deployment

To deploy this project run

```bash
  python3 main.py
```

