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

Rate_tide = table();

Rate_tide.Time = [1:48]';
Rate_tide.Liquid = WTMean.Vol_rate(201:248);
Rate_tide.Gas = repmat(0,size(Rate_tide,1),1);
Rate_tide.Energy = repmat(0,size(Rate_tide,1),1);


% one more step for PFLOTRAN input
% set soil surface as 3.11m
soil_surf = 3.11;
VolRate_t0 = (WTMean.WT(201) - soil_surf) .* Area .* Porosity;   %this is for PFLOTRAN

% In PFLOTRAN, we set the water saturation as 100% at t0, but if the actual
%  water level at the first timepoint is higher (or lower) than the soil surface, we
%  need to tell PFLOTRAN to add more (or reduce) water to the soil profile
%  at t0 to reach the actual observed water content

%% create flow rate list for O2 exchange at the sed_air_interface
Rate_O2 = table();
Rate_O2.WT = WTMean.WT(201:248);
Rate_O2.Time = [1:48]';

% When there is overlying water, no O2 exchange
% When the soil is not saturated with water, turn on O2 exchange with atm
% Less water, more O2 exchange


f = abs(soil_surf - Rate_O2.WT) ./ 0.1; %here use 0.1m as the reference point, if water level is 0.1m lower than the surface, turn on O2 exchange "in full power"
Rate_O2.Liquid = 1.d-5 .* f;
Rate_O2.Liquid (Rate_O2.WT > soil_surf) = 0; % if water table is higher than soil surface, turn off O2 exchange
Rate_O2.Liquid (Rate_O2.WT - soil_surf < -0.1 ) = 1.d-5;



Rate_O2.Gas = zeros(size(Rate_O2,1),1);
Rate_O2.Energy = zeros(size(Rate_O2,1),1);

%%
figure;
plot(Rate_O2.Liquid);hold on
yyaxis right
plot(WTMean.WT(201:248))
plot([0 48], [soil_surf soil_surf], 'k-')

%%
load("C:\Users\yz60069\TAI\TAI_fresh\WaterTableData.mat")

%%
writetable(WTMean, 'C:\Users\yz60069\TAI\TAI_fresh\WTMean.csv')