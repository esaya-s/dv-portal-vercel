# 🌐 Domain Setup Guide: anvilu.com → Vercel

## 📍 Current Status
- ✅ Application deployed to Vercel
- ⏳ Waiting for you to configure custom domain

## 🎯 Goal
Make your Django app accessible at **anvilu.com** (without any port numbers!)

---

## 📋 Step-by-Step Instructions

### Step 1: Access Vercel Dashboard
1. Go to: https://vercel.com/dashboard
2. Log in with your account
3. Find and click on your project: `dv-portal-vercel`

### Step 2: Add Custom Domain

1. In your project dashboard, click **Settings** (top navigation)
2. Click **Domains** in the left sidebar
3. You'll see "Add Domain" button - click it
4. Enter your domain: `anvilu.com`
5. Click **Add**

**Also Add WWW (Recommended):**
6. Click "Add Domain" again
7. Enter: `www.anvilu.com`
8. Click **Add**
9. Set `www.anvilu.com` to redirect to `anvilu.com` (or vice versa)

### Step 3: Get DNS Configuration

After adding the domain, Vercel will show you DNS records to add. It will look like:

```
┌─────────────────────────────────────────────────────┐
│ Configure DNS Records                                │
├─────────────────────────────────────────────────────┤
│                                                       │
│ Add these records to your DNS provider:              │
│                                                       │
│ Type: A                                              │
│ Name: @                                              │
│ Value: 76.76.21.21                                   │
│                                                       │
│ Type: CNAME                                          │
│ Name: www                                            │
│ Value: cname.vercel-dns.com                          │
│                                                       │
└─────────────────────────────────────────────────────┘
```

### Step 4: Update DNS at Your Domain Registrar

**Where did you buy anvilu.com?** (e.g., GoDaddy, Namecheap, Cloudflare, etc.)

#### Go to Your Domain Registrar's DNS Settings

##### If using Cloudflare:
1. Log in to Cloudflare
2. Select your domain: `anvilu.com`
3. Go to **DNS** → **Records**
4. Add/Update these records:

**Record 1 - Root Domain:**
```
Type: A
Name: @  (or leave blank for root)
IPv4 address: 76.76.21.21
Proxy status: DNS only (gray cloud)
TTL: Auto
```

**Record 2 - WWW Subdomain:**
```
Type: CNAME
Name: www
Target: cname.vercel-dns.com
Proxy status: DNS only (gray cloud)
TTL: Auto
```

##### If using GoDaddy/Namecheap/Other:
1. Log in to your domain registrar
2. Go to DNS Management or DNS Settings
3. Add/Update these records:

**Record 1:**
- Type: `A`
- Host: `@` (means root domain)
- Points to: `76.76.21.21`
- TTL: `Automatic` or `600`

**Record 2:**
- Type: `CNAME`
- Host: `www`
- Points to: `cname.vercel-dns.com`
- TTL: `Automatic` or `600`

### Step 5: Save and Wait

1. **Save** your DNS records
2. **Wait** for DNS propagation:
   - Can take: 10 minutes to 48 hours
   - Usually: 10-30 minutes
   - Cloudflare: Often 5-10 minutes

### Step 6: Verify in Vercel

1. Go back to Vercel Dashboard → Your Project → Settings → Domains
2. You should see your domain status change from:
   - ⏳ "Pending Verification" → ✅ "Valid Configuration"

---

## ✅ Testing Your Domain

### Check DNS Propagation
Open Command Prompt or PowerShell and run:
```bash
nslookup anvilu.com
```

You should see:
```
Name:    anvilu.com
Address: 76.76.21.21
```

### Visit Your Site
1. Open browser
2. Go to: `http://anvilu.com`
3. Should redirect to: `https://anvilu.com` (Vercel auto-adds HTTPS!)

---

## 🔒 HTTPS / SSL Certificate

**Good News:** Vercel automatically provides FREE SSL certificates!

- Vercel will automatically issue an SSL certificate for `anvilu.com`
- Usually takes 5-10 minutes after domain verification
- Your site will be accessible via `https://anvilu.com`
- HTTP requests are automatically redirected to HTTPS

---

## 🐛 Troubleshooting

### Domain Not Working After 30+ Minutes?

**Check DNS Records:**
```bash
# Check if A record is correct
nslookup anvilu.com

# Check if CNAME is correct  
nslookup www.anvilu.com
```

**Common Issues:**

1. **Wrong IP Address**
   - Make sure A record points to: `76.76.21.21`
   - Not your old server IP!

2. **Cloudflare Proxy Enabled**
   - If using Cloudflare, make sure proxy is OFF (gray cloud)
   - Or: Keep proxy ON but add Cloudflare as a custom domain in Vercel

3. **Old DNS Records**
   - Delete any old A records for `@` or `anvilu.com`
   - Delete any old CNAME for `www`

4. **Propagation Not Complete**
   - Check from different location: https://www.whatsmydns.net/
   - Enter: `anvilu.com`
   - Should show `76.76.21.21` globally

### Vercel Shows "Invalid Configuration"?

1. **Check DNS records are correct** (type, name, value)
2. **Wait longer** (DNS can take up to 48 hours)
3. **Remove and re-add domain** in Vercel
4. **Contact Vercel Support** if stuck

---

## 📊 Quick Reference

| Item | Value |
|------|-------|
| **Your Domain** | anvilu.com |
| **Vercel IP** | 76.76.21.21 |
| **Vercel CNAME** | cname.vercel-dns.com |
| **Expected Wait Time** | 10-30 minutes |
| **SSL Certificate** | Automatic (FREE) |
| **Deployment URL** | https://anvilu.com |

---

## 🎉 Success Checklist

- [ ] Added domain in Vercel Dashboard
- [ ] Updated A record at domain registrar
- [ ] Updated CNAME record for www
- [ ] Saved DNS changes
- [ ] Waited 10-30 minutes
- [ ] Verified domain in Vercel shows "Valid"
- [ ] Visited https://anvilu.com successfully
- [ ] SSL certificate is active (padlock icon in browser)

---

## 🚀 After Domain is Live

Once `anvilu.com` is working:

1. **Update Environment Variables** in Vercel:
   ```
   ALLOWED_HOSTS=anvilu.com,www.anvilu.com
   ```

2. **Test all pages** on your domain

3. **Set up redirects** (if needed):
   - `www.anvilu.com` → `anvilu.com` (or vice versa)
   - This is done in Vercel Dashboard → Domains

4. **Share your site!** 🎊
   - Your Django app is now live at: **https://anvilu.com**
   - No port numbers needed!
   - Professional SSL certificate!
   - Fast global CDN!

---

**Need Help?** Check the build logs in Vercel or refer to `VERCEL_NEXT_STEPS.md`

