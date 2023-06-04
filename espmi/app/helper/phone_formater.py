def change_phone_format(phone) -> str:
    if phone is None:
        return phone

    if phone.startswith('0'):
        phone = '62'+phone[1:]
    elif phone.startswith('8'):
        phone = '62'+phone

    if not phone.startswith('+'):
        phone = '+'+phone

    return phone
