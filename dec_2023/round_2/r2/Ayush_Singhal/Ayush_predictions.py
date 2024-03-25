# Training results can be seen on https://wandb.ai/ayushsinghal659/lightning_logs/runs/mjyo1mef?workspace=user-ayushsinghal659

# predictions_<team_lead_name>.py
from instructions import ETHPriceRanges

from enum import Enum
import pandas as pd 
import numpy as np 
import requests

from sklearn.preprocessing import StandardScaler

import torch 
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from pytorch_lightning import LightningDataModule as LDM
from pytorch_lightning import LightningModule as LM
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from pytorch_lightning import Trainer

import torch.nn as nn
def train():

    class data(Dataset) : 
    
        def __init__(self) : 
    
            super().__init__()
                
            self.X = np.load('Inputs.npy' , allow_pickle = True)
            self.y = np.load('Labels.npy' , allow_pickle = True)
            
        def __len__(self) : return self.X.shape[0]
    
        def __getitem__(self , index) : 
    
            r_embed = torch.tensor(self.X[index] , dtype = torch.float32)
            r_target = torch.tensor(self.y[index] , dtype = torch.float32)
    
            return r_embed , r_target
    
    class Data(LDM) : 
    
        def __init__(self , batch_size = 32) : 
    
            super().__init__()
    
            self.batch_size = batch_size
    
        def setup(self , stage = None) : self.train = data()
    
        def train_dataloader(self) : return DataLoader(self.train , batch_size = self.batch_size)
    
    data_module = Data()
    
    class lightning(LM) : 
    
        def __init__(self) : 
    
            super().__init__()
    
            self.lstm = nn.LSTM(input_size = 3 , hidden_size = 10 , num_layers = 50) 
            self.line = nn.Linear(10 , 1)
            self.loss_func = nn.MSELoss()
    
        def forward(self , inp) : 
    
            emb = self.lstm(inp)[1][0][0]
            emb = self.line(emb)
    
            return emb
    
        def training_step(self , batch , batch_idx) : 
    
            inputs , labels = batch
            outputs = self(inputs)
    
            loss = self.loss_func(outputs , labels)
            self.log('train_loss' , loss)
    
            return loss
    
        def configure_optimizers(self) : return torch.optim.Adam(self.parameters())
    
    checkpoint_callback = ModelCheckpoint(
        monitor='train_loss',
        filename='best_model',
        save_top_k=1,
        mode='min',
        save_weights_only=True,
    )
    early_stopping_callback = EarlyStopping(
        monitor='train_loss',
        patience=10,
        mode='min',
    )
    
    model = lightning()
    
    trainer = Trainer(
        max_epochs=1, 
        callbacks=[checkpoint_callback, early_stopping_callback])
    
    trainer.fit(model , data_module)

    return model
def predictions(train_model = True):
    print(train_model)
    
    if train_model:
    
        data = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=ETH&tsym=USD&limit=10&aggregate=1').json()['Data']['Data']
        data = pd.json_normalize(data)
        data = data[['high', 'low', 'open']]
        X_input = data.values
        
        scaler = StandardScaler()
        X_input_scaled = scaler.fit_transform(X_input)
        
        X_input_tensor = torch.tensor(X_input_scaled, dtype=torch.float32)
        
        model = train()
        
        model.eval()
        
        num_steps = 7
        predictions = []
        prices = []
        
        for index in range(num_steps):
        
            data_to_inverse_transform = np.vstack((X_input_tensor[-9:].numpy(), np.repeat(model(X_input_tensor[-10:]).detach().numpy(), 3, axis=0)))
            y_pred_single_original = scaler.inverse_transform(data_to_inverse_transform)
        
            predictions.append(y_pred_single_original[index])
        
            X_input = np.vstack((X_input, y_pred_single_original))
        
            X_input = X_input[-10:]
        
            prices.append(y_pred_single_original[index, 2])
    else : prices = [2369.83, 2360.64, 2366.76, 2360.17, 2356.28, 2362.1, 2374.02] # Use this prices if the training time is long
    
    return_val = []

    for val in prices : 
        if val >= 2000 and val < 2025 : return_val.append(ETHPriceRanges.pr_2000_2025)
        elif val >= 2025 and val < 2050 : return_val.append(ETHPriceRanges.pr_2025_2050)
        elif val >= 2050 and val < 2075 : return_val.append(ETHPriceRanges.pr_2050_2075)
        elif val >= 2075 and val < 2100 : return_val.append(ETHPriceRanges.pr_2075_2100)
        elif val >= 2100 and val < 2125 : return_val.append(ETHPriceRanges.pr_2100_2125)
        elif val >= 2125 and val < 2150 : return_val.append(ETHPriceRanges.pr_2125_2150)
        elif val >= 2150 and val < 2175 : return_val.append(ETHPriceRanges.pr_2150_2175)
        elif val >= 2175 and val < 2200 : return_val.append(ETHPriceRanges.pr_2175_2200)
        elif val >= 2200 and val < 2225 : return_val.append(ETHPriceRanges.pr_2200_2225)
        elif val >= 2225 and val < 2250 : return_val.append(ETHPriceRanges.pr_2225_2250)
        elif val >= 2250 and val < 2275 : return_val.append(ETHPriceRanges.pr_2250_2275)
        elif val >= 2275 and val < 2300 : return_val.append(ETHPriceRanges.pr_2275_2300)
        elif val >= 2300 and val < 2325 : return_val.append(ETHPriceRanges.pr_2300_2325)
        elif val >= 2325 and val < 2350 : return_val.append(ETHPriceRanges.pr_2325_2350)
        elif val >= 2350 and val < 2375 : return_val.append(ETHPriceRanges.pr_2350_2375)
        elif val >= 2375 and val < 2400 : return_val.append(ETHPriceRanges.pr_2375_2400)
        elif val >= 2400 and val < 2425 : return_val.append(ETHPriceRanges.pr_2400_2425)
        elif val >= 2425 and val < 2450 : return_val.append(ETHPriceRanges.pr_2425_2450)
        elif val >= 2450 and val < 2475 : return_val.append(ETHPriceRanges.pr_2450_2475)
        elif val >= 2475 and val < 2500 : return_val.append(ETHPriceRanges.pr_2475_2500)
        elif val >= 2500 and val < 2525 : return_val.append(ETHPriceRanges.pr_2500_2525)
        elif val >= 2525 and val < 2550 : return_val.append(ETHPriceRanges.pr_2525_2550)
        elif val >= 2550 and val < 2575 : return_val.append(ETHPriceRanges.pr_2550_2575)
        elif val >= 2575 and val < 2600 : return_val.append(ETHPriceRanges.pr_2575_2600)
        else : return_val.append(ETHPriceRanges.pr_2600_2625)
    
    return return_val


# DO NOT REMOVE
preds = predictions()
# preds = predictions(train_model = False)
print(preds)
assert len(preds) == 7
assert all([isinstance(val, ETHPriceRanges) for val in preds])
