import re
from email.utils import parseaddr

def validate_email(email):
    """Validate an email address."""
        try:
                # Basic validation using email.utils
                        real_name, addr = parseaddr(email)
                                if not addr:
                                            return False
                                            
                                                    # More robust validation using regular expressions
                                                            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                                                                    if not re.match(pattern, addr):
                                                                                return False
                                                                                
                                                                                        return True
                                                                                            except Exception as e:
                                                                                                    # Log the error or return an error message
                                                                                                            print(f"Error validating email: {str(e)}")
                                                                                                                    return Falset(model