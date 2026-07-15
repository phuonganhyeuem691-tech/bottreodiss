# Cấu hình giả lập các biến để file main.py không bị lỗi khi nạp import *
__all__ = ['spm_config', 'get_spm_status']

spm_config = {
    "status": "active",
    "version": "1.0.0"
}

def get_spm_status():
    return "Hệ thống bổ trợ hoạt động tốt"

