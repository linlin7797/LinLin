#!/usr/bin/env python3
"""
MIPS Assembly Emulator - Chạy code MIPS cho bài tính diện tích hình chữ nhật
"""

def run_dientich():
    print("Nhap chieu dai hinh chu nhat: ", end="")
    try:
        dai = float(input())
    except ValueError:
        print("Loi: Vui long nhap so thuc!")
        return
    
    print("Nhap chieu rong hinh chu nhat: ", end="")
    try:
        rong = float(input())
    except ValueError:
        print("Loi: Vui long nhap so thuc!")
        return
    
    # Tính diện tích = dài × rộng
    dientich = dai * rong
    
    print(f"Dien tich hinh chu nhat la: {dientich}")

if __name__ == "__main__":
    run_dientich()
