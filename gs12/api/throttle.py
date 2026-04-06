from rest_framework.throttling import UserRateThrottle

class NameRateThrottle(UserRateThrottle):
  scope = 'name'