# 🚀 Quick Start Guide - Run DV Portal on Your Computer

This guide will help you get the DV Portal Ethiopia website running on your local computer so you can see the beautiful styling and test all features.

## 📋 Prerequisites

Make sure you have these installed on your computer:

- **Python 3.8 or higher** ([Download here](https://www.python.org/downloads/))
- **Git** (optional, for updates)
- **Text editor** (VS Code, Notepad++, etc.)

## ⚡ Super Quick Start (Recommended)

### Method 1: Using the Automated Script

1. **Open Terminal/Command Prompt** in the project folder
2. **Run the startup script**:
   ```bash
   python run_dev_server.py
   ```
3. **Follow the prompts** - the script will:
   - Create .env file automatically
   - Set up the database
   - Create admin user (optional)
   - Start the server

4. **Open your browser** and go to: `http://localhost:8000`

That's it! 🎉

---

## 🔧 Manual Setup (If you prefer step-by-step)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Environment
```bash
# Copy the environment template
copy env_example.txt .env     # Windows
cp env_example.txt .env       # Mac/Linux
```

### Step 3: Set Up Database
```bash
python manage.py migrate
```

### Step 4: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### Step 5: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 6: Start the Server
```bash
python manage.py runserver
```

### Step 7: Open in Browser
Go to: `http://localhost:8000`

---

## 🌐 What You'll See

### 🏠 Homepage Features:
- **Professional government-style design** similar to US DV website
- **Hero section** with Ethiopian and US flags
- **Step-by-step process** guide
- **Feature highlights** (AI validation, Telegram bot, etc.)
- **Statistics** and announcements
- **Responsive design** that works on mobile

### 🔐 User Features:
- **Registration/Login** system
- **Dashboard** with application tracking
- **Profile management** with Ethiopian-specific fields
- **Application forms** (placeholder for now)
- **Payment system** with multiple methods

### 👨‍💼 Admin Features:
- **Admin panel** at `/admin` (if you created superuser)
- **User management**
- **Application tracking**
- **Payment verification**
- **System settings**

---

## 🎨 Styling Highlights

The website features:

- **🇺🇸 Government-style color scheme** (blue, white, red accents)
- **Professional typography** with Inter font
- **Bootstrap 5** responsive framework
- **Custom CSS** for DV-specific styling
- **Smooth animations** and hover effects
- **Mobile-friendly** responsive design
- **Accessibility features**
- **Clean, modern layout**

---

## 🔗 Main URLs to Explore

Once the server is running, visit these URLs:

| URL | Description |
|-----|-------------|
| `http://localhost:8000/` | Homepage with beautiful styling |
| `http://localhost:8000/accounts/register/` | User registration |
| `http://localhost:8000/accounts/login/` | User login |
| `http://localhost:8000/dashboard/` | User dashboard (after login) |
| `http://localhost:8000/about/` | About page |
| `http://localhost:8000/eligibility/` | Eligibility requirements |
| `http://localhost:8000/privacy-policy/` | Privacy policy |
| `http://localhost:8000/terms-of-service/` | Terms of service |
| `http://localhost:8000/admin/` | Admin panel (if superuser created) |

---

## 📱 Test the Features

### 1. Registration & Login
- Create a new user account
- See the beautiful registration form
- Login and access the dashboard

### 2. Dashboard
- View the professional dashboard layout
- See application cards and statistics
- Check the sidebar with quick actions

### 3. Responsive Design
- Resize your browser window
- Check on mobile device
- See how the layout adapts

### 4. Admin Panel
- If you created a superuser, login to `/admin`
- Explore the comprehensive admin features
- See user management capabilities

---

## 🛠️ Customization (Optional)

### Change Colors
Edit `templates/base.html` and modify the CSS variables:
```css
:root {
    --primary-blue: #1e3a8a;    /* Main blue color */
    --secondary-blue: #3b82f6;  /* Secondary blue */
    --light-blue: #dbeafe;      /* Light blue */
    /* ... */
}
```

### Add Your Logo
Replace the text logo in `templates/base.html`:
```html
<a class="navbar-brand" href="{% url 'core:home' %}">
    <img src="your-logo.png" alt="Logo" height="40">
    DV Portal Ethiopia
</a>
```

---

## ❓ Troubleshooting

### Port Already in Use
If you see "Port 8000 is already in use":
```bash
python manage.py runserver 8080
```
Then visit: `http://localhost:8080`

### Permission Errors
On Windows, if you get permission errors:
```bash
python -m pip install -r requirements.txt --user
```

### Module Not Found
Make sure you're in the correct directory:
```bash
cd path/to/dv-portal-ethiopia
python manage.py runserver
```

### CSS Not Loading
Run this command:
```bash
python manage.py collectstatic --clear
```

---

## 🎯 Next Steps

After exploring the styling:

1. **Add API Keys** (optional):
   - Edit `.env` file
   - Add Telegram bot token
   - Add Gemini AI API key

2. **Customize Content**:
   - Update homepage text
   - Modify announcements
   - Add your contact information

3. **Test Full Features**:
   - Payment system
   - Telegram integration
   - AI validation

4. **Deploy to Production**:
   - Follow `CPANEL_DEPLOYMENT.md`
   - Set up domain and SSL

---

## 🎉 Enjoy Exploring!

The website is fully functional with:
- ✅ Beautiful, professional styling
- ✅ Government-inspired design
- ✅ Responsive mobile layout
- ✅ Complete user system
- ✅ Admin management
- ✅ Database integration
- ✅ Security features

Take your time exploring all the pages and features. The styling is designed to give users confidence in the professional service while maintaining the familiar look of official US government websites.

**Happy exploring! 🇺🇸🇪🇹**
