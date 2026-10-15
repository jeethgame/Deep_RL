% Load MobileNetV2
net = mobilenetv2;
disp(net);

% Load GoogLeNet
net = googlenet;
disp(net);

% Create and train RNN
[X,T] = simpleseries_dataset;
net = layrecnet(1:2,10);
[Xs,Xi,Ai,Ts] = preparets(net,X,T);
net = train(net,Xs,Ts,Xi,Ai);
view(net);