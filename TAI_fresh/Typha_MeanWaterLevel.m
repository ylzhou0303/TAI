% Typha site water table data processing

% import
WT = readtable('C:\MBL\Research\Typha data\water table\CB_continuous_pt_corrected.csv');
WT.Properties.VariableNames{6} = 'WaterTable';
WT.Properties.VariableNames{2} = 'DT';

%%

figure;
plot(WT.DT, WT.WaterTable)

%% calculate hourly mean
WTMean = table();
k = 1;

temp_list = [];
temp_list(1) = WT.WaterTable(1);
j = 2;

for i = 2:size(WT,1)
    time_prev = datestr(WT.DT(i-1),'dd/mmm/yyyy HH:MM:SS');
    time_curr = datestr(WT.DT(i),'dd/mmm/yyyy HH:MM:SS');
    
    
    if strcmp(time_curr(13:14), time_prev(13:14))
        temp_list(j) = WT.WaterTable(i);
        j = j + 1;
    else
        WTMean.DT(k) = cellstr(time_prev);
        WTMean.WT(k) = mean(temp_list, 'omitnan');
        k = k + 1;

        temp_list = [];
        temp_list(1) = WT.WaterTable(i);
        j = 2;
    end
end

%% create constraint list for PFLOTRAN
WTMean.Constraint (~(WTMean.WT < 0.95)) = cellstr('sed_water_interface'); 
%when water table is higher than 0.95, which is the soil surface, the constraint is
%sed_water_interface

WTMean.Constraint(WTMean.WT < 0.95) = cellstr('sed_air_interface');

%%
Constraint_List = table();
Constraint_List.Timepoint = [0:336]';
Constraint_List.Constraint = WTMean.Constraint(73:409);
