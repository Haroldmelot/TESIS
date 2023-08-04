
from steps import (
    retrieval,
    expenses, 
    schedule, 
    prediction
)


transformed_data = retrieval.transform_data()

scheduled = schedule.schedule_resources(transformed_data)

prediction = prediction.generate_prediction(scheduled)
expenses = expenses.calculate_time_spent(scheduled)

## Here join prediction and expenses data
# into a format that can be stored on csv
# usgin `store_data` from `utils`
