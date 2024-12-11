
import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")
recipient_name = input("Enter Recipient Name: ")

# Example parameters for UPI payment (you can modify them as needed)
amount = input("Enter Amount: ")
currency = "INR"
message = "Payment"

# UPI payment URLs
phonepe_url = f'upi://pay?pa={upi_id}&rn={recipient_name}&am={amount}&cu={currency}&msg={message}'
paytm_url = f'upi://pay?pa={upi_id}&rn={recipient_name}&am={amount}&cu={currency}&msg={message}'
google_pay_url = f'upi://pay?pa={upi_id}&rn={recipient_name}&am={amount}&cu={currency}&msg={message}'

# Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR codes as image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (requires the PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()