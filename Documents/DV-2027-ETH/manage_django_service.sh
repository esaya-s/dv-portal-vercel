#!/bin/bash
echo "🔄 Managing Django Service (no root access)..."
echo "================================================"

case "$1" in
    start)
        echo "🚀 Starting Django service..."
        nohup gunicorn --bind 0.0.0.0:8080 --workers 3 --timeout 120 --daemon dv_portal.wsgi:application
        echo "✅ Django service started on port 8080"
        echo "🌐 Access: http://anvilu.com:8080"
        ;;
    stop)
        echo "🛑 Stopping Django service..."
        pkill -f "gunicorn.*dv_portal.wsgi"
        echo "✅ Django service stopped"
        ;;
    restart)
        echo "🔄 Restarting Django service..."
        pkill -f "gunicorn.*dv_portal.wsgi"
        sleep 2
        nohup gunicorn --bind 0.0.0.0:8080 --workers 3 --timeout 120 --daemon dv_portal.wsgi:application
        echo "✅ Django service restarted on port 8080"
        ;;
    status)
        echo "📊 Checking Django service status..."
        if pgrep -f "gunicorn.*dv_portal.wsgi" > /dev/null; then
            echo "✅ Django service is running on port 8080"
            echo "🌐 Access: http://anvilu.com:8080"
        else
            echo "❌ Django service is not running"
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        echo ""
        echo "Examples:"
        echo "  $0 start    - Start Django service"
        echo "  $0 stop     - Stop Django service"
        echo "  $0 restart  - Restart Django service"
        echo "  $0 status   - Check service status"
        exit 1
        ;;
esac
