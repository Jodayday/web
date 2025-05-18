from django.shortcuts import render
from django.db.models import Count
from visitor.models import VisitorLog
from django.utils import timezone
from datetime import timedelta

def stats(request):
    today = timezone.now().date()

    # 전체 방문 횟수
    total_visits = VisitorLog.objects.count()

    # 고유 IP 수
    
    unique_ips   = VisitorLog.objects.values('ip_address').distinct().count()
    # 고유 IP 목록
    unique_ip_list = (
        VisitorLog.objects
        .values_list('ip_address', flat=True)
        .distinct()
    )
    # 최근 7일간 일별 방문 횟수
    week_ago = today - timedelta(days=6)
    qs = (
        VisitorLog.objects
        .filter(timestamp__date__gte=week_ago)
        .extra({"day": "date(timestamp)"})
        .values("day")
        .annotate(visits=Count("id"))
        .order_by("day")
    )

    # 템플릿으로 전달
    context = {
        "total_visits": total_visits,
        "unique_ips": unique_ips,
        'unique_ip_list': unique_ip_list,
        "daily_stats": qs,  # queryset of {"day": date, "visits": int}
    }
    return render(request, "visitor/stats.html", context)
