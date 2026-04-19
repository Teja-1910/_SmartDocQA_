//  Email validation
export const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

// Password validation (min 6 chars)
export const validatePassword = (password) => {
  return password && password.length >= 6;
};

//  Block personal emails
export const isCompanyEmail = (email) => {
  const blocked = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"];

  const domain = email.split("@")[1]?.toLowerCase();

  return !blocked.includes(domain);
};
