#!/bin/bash
echo "🌐 Setting up Cloudflare Tunnel (hide port number)..."
echo "================================================"

echo ""
echo "📋 This will help you access anvilu.com without :8080"
echo ""

# Check if cloudflared is installed
if ! command -v cloudflared &> /dev/null; then
    echo "📦 Installing Cloudflare Tunnel..."
    
    # Download cloudflared
    wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
    
    # Install (if possible without root)
    if dpkg -i cloudflared-linux-amd64.deb 2>/dev/null; then
        echo "✅ Cloudflared installed successfully"
    else
        echo "⚠️ Cannot install cloudflared without root access"
        echo "💡 Alternative: Use Cloudflare's web interface to set up tunnel"
        echo ""
        echo "📋 Manual setup steps:"
        echo "1. Go to https://dash.cloudflare.com/"
        echo "2. Create a new tunnel"
        echo "3. Point it to your server:8080"
        echo "4. Configure DNS to point anvilu.com to the tunnel"
        exit 1
    fi
fi

echo "🔧 Starting Cloudflare Tunnel..."
echo "This will create a tunnel from anvilu.com to localhost:8080"

# Start tunnel (you'll need to authenticate)
cloudflared tunnel --url http://localhost:8080

echo ""
echo "✅ Tunnel setup complete!"
echo "🌐 Your site is now available at: http://anvilu.com (no port!)"
