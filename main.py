
from steps import (
    retrieval,
    expenses, 
    schedule, 
    prediction
)


transformed_data = retrieval.transform_data()

scheduled_data = schedule.schedule_resources(transformed_data)

prediction_data = prediction.generate_prediction(scheduled_data)
expenses_data = expenses.calculate_time_spent(scheduled_data)

## Here join prediction and expenses data
# into a format that can be stored on csv
# usgin `store_data` from `utils`
