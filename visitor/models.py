from django.db import models

class VisitorLog(models.Model):
    ip_address = models.GenericIPAddressField()   # IPv4, IPv6 지원
    path       = models.CharField(max_length=255) # 요청된 URL 경로
    user_agent = models.CharField(max_length=512, blank=True)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} → {self.path} @ {self.timestamp}"
