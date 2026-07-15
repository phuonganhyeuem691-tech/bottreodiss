import sys

class SpmModule(object):
    def __getattr__(self, name):
        # Tự động tạo ra hàm ảo cho bất kỳ tên hàm nào được gọi (ví dụ: send_otp_via_dienmayxanh)
        if name.startswith('send_otp_via_'):
            def dummy_func(*args, **kwargs):
                print(f"[spm] Đã chặn lỗi và chạy hàm ảo: {name}")
                return False
            return dummy_func
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

sys.modules[__name__] = SpmModule()
