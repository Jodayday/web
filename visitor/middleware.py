import logging
from django.utils.deprecation import MiddlewareMixin
from .models import VisitorLog

logger = logging.getLogger(__name__)

class VisitorLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 1) 실제 클라이언트 IP 가져오기 (프록시가 있을 경우)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")

        # 2) User-Agent
        ua = request.META.get("HTTP_USER_AGENT", "")

        # 3) DB에 저장 (에러 방지를 위해 try/except)
        try:
            VisitorLog.objects.create(
                ip_address=ip,
                path=request.path,
                user_agent=ua
            )
        except Exception as e:
            logger.error(f"VisitorLog 생성 실패: {e}")
        # 다음 미들웨어/뷰로 진행
