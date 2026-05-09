from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    page_size = 50
    page_size_query_param = "limit"
    cursor_query_param = "cursor"
    max_page_size = 100
    ordering = ("-_created_at", "-id")  

    def get_paginated_response(self, data):
        return Response({
            "next_cursor": self.get_next_link(),     
            "previous_cursor": self.get_previous_link(),
            "results": data,
        })

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "next_cursor": {"type": "string", "nullable": True},
                "previous_cursor": {"type": "string", "nullable": True},
                "results": schema,
            },
        }