
% A + B -> C, with constant input of A

Homo_A = zeros(100,100);
Homo_B = ones(100,100) * 100;

Het_A = zeros(100,100);
Het_B = ones(100,100) * 100;

r_Homo = zeros(100,100);
r_Het = zeros(100,100);


v = 10;  %total input rate of A

v_Homo = v / 100;


root_cells = 1:15;
v_Het = zeros(100,1);
v_Het(root_cells,1) = v/15; 

K_A = 10;  %half saturation constant
K_B = 5;

for i = 2:1000
    r_Homo(:, i-1) = Monod(Homo_A(:,i-1),K_A) .* Monod(Homo_B(:, i-1), K_B);
    Homo_A(:, i) = Homo_A(:, i-1) + v_Homo - r_Homo(:,i-1);
    Homo_B(:, i) = Homo_B(:, i-1) - r_Homo(:,i-1);
    
    r_Het(:, i-1) = Monod(Het_A(:,i-1),K_A) .* Monod(Het_B(:, i-1), K_B);
    Het_A(:, i) = Het_A(:, i-1) + v_Het - r_Het(:,i-1);
    Het_B(:, i) = Het_B(:, i-1) - r_Het(:, i-1);
    
end


%% Plot the Monod and concentration relationship
timepoint = 9999;

figure;
x = 0:70;
y = Monod(x,K);

Pcoef = corr(x',y', 'type','Pearson')  %calculate the Pearson's correlation coefficient
plot(x, y, 'r-');hold on      %Monod curve

plot(Het(:,timepoint), r_Het(:,timepoint), 'ro');   %Het Mode rate and concentration

plot(mean(Het(:,timepoint)), mean(r_Het(:,timepoint)), 'r*'); %Het Mode mean rate

plot(mean(Het(:,timepoint)), Monod(mean(Het(:,timepoint)),K), 'k*');  % rate calculated from the mean of concentration of Het
 
plot(mean(Homo(:,timepoint)), mean(r_Homo(:,timepoint)), 'b*');  %rate of Homo

ylim([0 1])
title({['K=',num2str(K)],['TimePoint: ',num2str(timepoint)]})

xlabel('Concentration')
ylabel('Monod rate')


%% Plot the time series of Homo and Het concentration
figure;
plot(mean(Homo,1),'b-');hold on
plot(mean(Het,1),'r-')

xlabel('Timepoint')
ylabel('Concentration')

%%
figure;
plot(mean(r_Homo,1), 'b-');hold on
plot(mean(r_Het,1), 'r-')

xlabel('Timepoint')
ylabel('Monod rate')

%% Plot the time series of difference in mean concentration
figure;
plot(mean(Het,1) - mean(Homo,1),'b-')

%%
x = 40:70;
t = 100;
y = x + K*log(x) - t;

figure;
plot(x, y,'b-');hold on
plot([40 70],[0 0],'k-')

%%
x = 0:100;
t = -x - K*log(x);
figure;
plot(t,x,'b-')


%%
k = 1;
O2_homo = 0.01 *v * K /(k-0.01*v);

O2_het = 0.15 * 1/15 * v * K /(k - 1/15*v);


Diff = O2_het - O2_homo;


%%
v = 10;
k = 0:0.1:10;

Diff = 0.01 * 10 * v .* (1./(k-0.067*v) - 1./(k - 0.01*v));

figure;
plot(k, Diff,'b.-');


%%
x = 0:100;
y = 1 ./ (x + 10);
figure;
plot(x, y, 'b-'); hold on

y2 = 1 ./ (x + 100);
plot(x, y2, 'r-')

y3 = 1 ./ (x + 1);
plot(x, y3, 'k-')

%%
function rates = Monod(conc, K)
    rates = conc./(conc + K);
end



