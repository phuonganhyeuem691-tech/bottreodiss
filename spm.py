# Danh sách định nghĩa tất cả các hàm gửi OTP có trong bộ code spam
def send_otp_via_sapo(*args, **kwargs): return False
def send_otp_via_viettel(*args, **kwargs): return False
def send_otp_via_medicare(*args, **kwargs): return False
def send_otp_via_tv360(*args, **kwargs): return False
def send_otp_via_dienmayxanh(*args, **kwargs): return False
def send_otp_via_concung(*args, **kwargs): return False
def send_otp_via_shopee(*args, **kwargs): return False
def send_otp_via_lazada(*args, **kwargs): return False
def send_otp_via_tiki(*args, **kwargs): return False
def send_otp_via_bachhoaxanh(*args, **kwargs): return False
def send_otp_via_fpt(*args, **kwargs): return False
def send_otp_via_grab(*args, **kwargs): return False

# Cho phép lệnh "from spm import *" nạp thành công toàn bộ hàm mà không báo lỗi NameError
__all__ = [
    'send_otp_via_sapo', 'send_otp_via_viettel', 'send_otp_via_medicare', 'send_otp_via_tv360',
    'send_otp_via_dienmayxanh', 'send_otp_via_concung', 'send_otp_via_shopee', 'send_otp_via_lazada',
    'send_otp_via_tiki', 'send_otp_via_bachhoaxanh', 'send_otp_via_fpt', 'send_otp_via_grab'
]
