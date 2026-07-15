# Giả lập các hàm gửi OTP để file main.py không bị lỗi NameError
def send_otp_via_sapo(*args, **kwargs): return False
def send_otp_via_viettel(*args, **kwargs): return False
def send_otp_via_medicare(*args, **kwargs): return False
def send_otp_via_tv360(*args, **kwargs): return False

# Thêm cấu hình xuất tất cả hàm ra ngoài
__all__ = [
    'send_otp_via_sapo', 
    'send_otp_via_viettel', 
    'send_otp_via_medicare', 
    'send_otp_via_tv360'
]
