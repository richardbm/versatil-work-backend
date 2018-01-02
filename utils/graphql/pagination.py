from math import fabs


def paginate_queryset(qs, **kwargs):
    max_limit = 20
    count = qs.count()
    limit = kwargs.get("limit", 0)

    if not limit:
        raise Exception("limit is required")
    ret = int(limit)

    limit = min(ret, max_limit)

    if limit is None:
        return None

    if limit < 0:
        offset = kwargs.get("offset", count) + limit
    else:
        offset = kwargs.get("offset", 0)

    if count == 0 or offset > count or offset < 0:
        return []

    return qs[offset:offset + fabs(limit)]


def paginate(activity, kwargs):
    limit = kwargs.get("limit", None)
    offset = kwargs.get("offset", None)
    if limit is not None and offset is not None:
        activity = paginate_queryset(activity,
                                     limit=limit,
                                     offset=offset)
    return activity
