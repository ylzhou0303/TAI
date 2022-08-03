% This script calculates the hoourly mean of water table level

cd('C:\Users\yz60069\Desktop')
Data = readtable('MAR-PR-Wtable-T-2012.xls','Sheet','MAR-PR-Wtable-T-2012');

%%
WT = Data(:,[1 2 11]);
WT.Date = WT.Date + (datetime('01-Jan-2022 00:00:01') - datetime('01-Jan-2022 00:00:00'));


%%
WTMean = table();
k = 1;

temp_list = [];
temp_list(1) = WT.Logger5Dc_m_(1);
j = 2;

for i = 2:size(WT,1)
    date_prev = datestr(WT.Date(i-1));
    date_curr = datestr(WT.Date(i));
    
    
    if strcmp(date_curr(13:14), date_prev(13:14))
        temp_list(j) = WT.Logger5Dc_m_(i);
        j = j + 1;
    else
        WTMean.Date(k) = datetime([date_prev(1:14), ':30:00']);
        WTMean.WT(k) = mean(temp_list);
        k = k + 1;

        temp_list = [];
        temp_list(1) = WT.Logger5Dc_m_(i);
        j = 2;
    end
end


%% calculate the change rate
WTMean.Rate(1:5278) = WTMean.WT(2:end) - WTMean.WT(1:end-1);  % the rate of water table level changes, unit: m/hr

%%
figure;
plot(WTMean.Date, WTMean.WT)


%% generate the rate list
Porosity = 0.25;
Area = 1 * 1;
WTMean.Vol_rate = WTMean.Rate .* Area .* Porosity;  
%convert the rate of water level change into volumetric rate of water addition/removal, accounting for the porosity

Rate_List = table();

Rate_List.Time = [1:48]';
Rate_List.Liquid = WTMean.Vol_rate(201:248);
Rate_List.Gas = repmat(0,size(Rate_List,1),1);
Rate_List.Energy = repmat(0,size(Rate_List,1),1);


% one more step for PFLOTRAN input
% set soil surface as 3.11m
soil_surf = 3.11;
VolRate_t0 = (WTMean.WT(201) - soil_surf) .* Area .* Porosity;   %this is for PFLOTRAN

% In PFLOTRAN, we set the water saturation as 100% at t0, but if the actual
%  water level at the first timepoint is higher than the soil surface, we
%  need to tell PFLOTRAN to add more water to the soil profile



%%
load("C:\Users\yz60069\TAI\TAI_fresh\WaterTableData.mat")

%%
writetable(WTMean, 'C:\Users\yz60069\TAI\TAI_fresh\WTMean.csv')