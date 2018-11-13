class RecentAnnoDominiConverter:
    regex = "20[01][0-9]"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value
        # return str(value)でも行ける

