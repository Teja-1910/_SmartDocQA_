def extract_company_from_email(email: str):
    try:
        return email.split("@")[1].split(".")[0].lower().strip()
    except:
        return "unknown"


def extract_company_from_filename(filename: str):
    return filename.split(".")[0].lower().strip()