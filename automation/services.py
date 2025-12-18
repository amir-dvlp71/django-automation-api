import pandas as pd
from django.core.files.base import ContentFile
import io

def process_file(job):
    """
    job: AutomationJob instance
    """

    job.status = 'processing'
    job.save()

    try:
        # 1. Read file
        file_path = job.file.path

        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        # 2. Clean data
        df = df.dropna()             
        df.columns = [c.lower() for c in df.columns]  

       
        df['total'] = df['price'] * df['quantity']

        # 3. Generate report
        report = {
            "rows": len(df),
            "total_sum": float(df['total'].sum()),
            "average_price": float(df['price'].mean())
        }

        # 4. Save cleaned CSV
        buffer = io.StringIO()
        df.to_csv(buffer, index=False)

        job.result_file.save(
            f"result_{job.id}.csv",
            ContentFile(buffer.getvalue())
        )

        job.report = report
        job.status = 'done'
        job.save()

    except Exception as e:
        job.status = 'failed'
        job.report = {"error": str(e)}
        job.save()
