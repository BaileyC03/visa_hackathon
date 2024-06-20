import pandas as pd

def overall_score(cluster_name_adjusted):
    # Read the data from the CSV file
    data = pd.read_csv('..\data\Visa Climate Tech Data.xlsx - 2_Card data.csv')


    transportation = ['PARKING LOTS,METERS,GARAGES', 'PASSENGER RAILWAYS', 'TAXICABS/LIMOUSINES', 'BUS LINES', 'TAX PAYMENTS', 'UTILITIES/ELEC/GAS/H2O/SANI', 'SERVICE STATIONS', 'COMMERCIAL EQUIPMENT - DEFAULT', 'LOCAL COMMUTER TRANSPORT']

    # only keep the rows where the 'mrch_catg_rlup_nm' column is in the transportation list
    data = data[data['mrch_catg_rlup_nm'].isin(transportation)]

    # convert all the values in the cpd_dt column to datetime
    data['cpd_dt'] = pd.to_datetime(data['cpd_dt'])
    #oldest date in the dataset
    start_date = data['cpd_dt'].min()
    #latest date in the dataset
    end_date = data['cpd_dt'].max()
    
    public_transport = ['PASSENGER RAILWAYS', 'BUS LINES', 'LOCAL COMMUTER TRANSPORT']
    private_transport = ['PARKING LOTS,METERS,GARAGES', 'TAXICABS/LIMOUSINES', 'SERVICE STATIONS', 'COMMERCIAL EQUIPMENT - DEFAULT']

    cluster_data = data[data['cluster_name_adjusted'] == cluster_name_adjusted]
    
    # filter the data to include only the rows where the 'cpd_dt' column is between the start_date and end_date parameters
    date_filtered_data = cluster_data[(cluster_data['cpd_dt'] >= start_date) & (cluster_data['cpd_dt'] <= end_date)]
    
    # filter the data to include only the rows where the 'mrch_catg_rlup_nm' column is in the public_transport list
    public_transport_data = date_filtered_data[date_filtered_data['mrch_catg_rlup_nm'].isin(public_transport)]
    
    # filter the data to include only the rows where the 'mrch_catg_rlup_nm' column is in the private_transport list
    private_transport_data = date_filtered_data[date_filtered_data['mrch_catg_rlup_nm'].isin(private_transport)]
    
    # calculate the total amount spent on public transport
    total_public_transport_spent = public_transport_data['spend'].sum()
    
    # calculate the total amount spent on private transport
    total_private_transport_spent = private_transport_data['spend'].sum()
    
    return total_public_transport_spent, total_private_transport_spent