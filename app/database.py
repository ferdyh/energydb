import duckdb
import itertools

from app.models import Metric, Meter

class Database():
    def __init__(self):
        self.conn = duckdb.connect("./metrics.db", read_only=True)

    def get_month_metrics(self):
        # return self.conn.query("select * from metrics").fetchall()
        results = self.conn.query("""
            select
                meter, 
                date_trunc('day', timestamp) date,
                max(value) - min(value) usage 
            from metrics 
            where date_trunc('month', timestamp) = '2023-04-01'
            group by meter, date_trunc('day', timestamp)
            order by date
            """).fetchall()
        
        return self.format_metrics(results)
    
    def get_day_metrics(self):
        results = self.conn.query("""
        
        """).fetchall()

        return self.format_metrics(results)
        

    def format_metrics(self, rows):
        labels = { r[1] for r in rows }
        meters = []
        for k, g in itertools.groupby(sorted(rows, key=lambda s: s[0]), lambda r: r[0]):
            metrics = list(map(lambda v: v[2], g))

            if k == 31:
                name = "Grid (Low)"
                source = "grid"
            elif k == 32:
                name = "Grid (Normal)"
                source = "grid"
            elif k == 33:
                name = "Solar (Low)"
                source = "solar"
            else:
                name = "Solar (Normal)"
                source = "solar"
        

            m = Meter(meter=name, source=source, metrics=metrics)
            meters.append(m)

        # res = list(map(lambda k, g: k, out))

        return {
            "labels": sorted(labels),
            "data": meters
        }
        


# { 
#     labels: ["25-01-2023", "25-01-2023", "25-01-2023"]
#     meters: {
#         24: [0, 1, 2,3]
#     }
# }