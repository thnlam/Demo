### Import all the necessary Modules
import get_all_variables as gav
from create_spark_objects import get_spark_object
from validations import get_current_date

def main():
    print(gav.header)
    ### Get all variables

    ### Get Spark Object
    spark = get_spark_object(gav.envn,gav.appName)
    print("Spark Object is created...")
    # Validate Spark Object
    get_current_date(spark)
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_data_ingest script
        # Load stats file
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

    ### Initiate run_data_transform script
        # Load stats file
        # Validate
        # Set up Logging Configuration Mechanism
        # Set up Error Handling

if __name__ == "__main__" :
    main()